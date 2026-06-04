#!/usr/bin/env python3
"""Monta una posizione di Go (SGF 15x15) sullo stemma del Circolo Goistico Padovano.

Il reticolo di stelle dorate dello stemma e' gia' un goban 15x15 ruotato di 45 gradi:
ogni stella coincide con un'intersezione. Questo script poggia le pietre sugli incroci,
SOTTO le stelle (che restano visibili e fanno da marcatore sulle pietre).

Uso:
    python3 monta_partita.py PARTITA.sgf [-o OUT.svg] [-m N_MOSSE] [--base STEMMA.svg]

  -m N   monta la posizione fino alla mossa N (default: tutte -> posizione finale).
  Funziona con qualsiasi SGF di dimensione 15 (SZ[15]); con catture corrette.
"""
import argparse, re, sys

# --- geometria stemma (viewBox 680x606, campo 493x493 da 93.5,61.5) ---
N = 15
ORIGIN_X, ORIGIN_Y, STEP = 340, 70, 17  # x=340+STEP*(c-r) ; y=70+STEP*(c+r)
STONE_R = 10.8                            # passo tra vicini = STEP*sqrt(2) ~ 24
STARS_MARKER = '<rect x="93.5" y="61.5" width="493" height="493" fill="url(#stars)"'

GRADS = (
    '<radialGradient id="stoneB" cx="38%" cy="32%" r="78%"><stop offset="0" stop-color="#6b7079"/>'
    '<stop offset=".4" stop-color="#2a2e36"/><stop offset="1" stop-color="#090b0f"/></radialGradient>\n'
    '<radialGradient id="stoneW" cx="38%" cy="30%" r="82%"><stop offset="0" stop-color="#ffffff"/>'
    '<stop offset=".68" stop-color="#edeff2"/><stop offset="1" stop-color="#c5cad1"/></radialGradient>\n'
)


def parse_sgf(text, limit=None):
    """Ritorna la posizione finale (lista di (col, row, 'B'|'W')) applicando le catture."""
    if 'SZ[15]' not in text.replace(' ', ''):
        print("Attenzione: l'SGF non dichiara SZ[15]; la mappatura assume 15x15.", file=sys.stderr)
    moves = re.findall(r';([BW])\[([a-o]{2})\]', text)
    if limit is not None:
        moves = moves[:limit]
    board = [[None] * N for _ in range(N)]

    def neighbours(x, y):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                yield nx, ny

    def group(x, y):
        colour = board[y][x]
        stack, seen, cells, libs = [(x, y)], {(x, y)}, [], 0
        while stack:
            cx, cy = stack.pop()
            cells.append((cx, cy))
            for nx, ny in neighbours(cx, cy):
                v = board[ny][nx]
                if v is None:
                    libs += 1
                elif v == colour and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    stack.append((nx, ny))
        return cells, libs

    for colour, coord in moves:
        x, y = ord(coord[0]) - 97, ord(coord[1]) - 97
        board[y][x] = colour
        opp = 'W' if colour == 'B' else 'B'
        for nx, ny in neighbours(x, y):
            if board[ny][nx] == opp:
                cells, libs = group(nx, ny)
                if libs == 0:
                    for gx, gy in cells:
                        board[gy][gx] = None
    return [(x, y, board[y][x]) for y in range(N) for x in range(N) if board[y][x]]


def stones_group(stones):
    out = ['<g id="goban-stones">']
    for c, r, colour in stones:
        cx = ORIGIN_X + STEP * (c - r)
        cy = ORIGIN_Y + STEP * (c + r)
        if colour == 'B':
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{STONE_R}" fill="url(#stoneB)" stroke="#05070a" stroke-width="0.6"/>'
                       f'<ellipse cx="{cx-3.4}" cy="{cy-3.8}" rx="3.4" ry="2.3" fill="#aeb4bd" opacity="0.5"/>')
        else:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{STONE_R}" fill="url(#stoneW)" stroke="#9aa0a8" stroke-width="0.6"/>'
                       f'<ellipse cx="{cx-3.4}" cy="{cy-3.8}" rx="3.6" ry="2.4" fill="#ffffff" opacity="0.85"/>')
    out.append('</g>')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('sgf')
    ap.add_argument('-o', '--out')
    ap.add_argument('-m', '--moves', type=int, help='monta fino alla mossa N (default: tutte)')
    ap.add_argument('--base', default='logo_circolo_goistico_padovano_completo.svg')
    args = ap.parse_args()

    stones = parse_sgf(open(args.sgf, encoding='utf-8').read(), args.moves)
    nb = sum(1 for *_, c in stones if c == 'B')
    nw = len(stones) - nb

    svg = open(args.base, encoding='utf-8').read()
    if svg.count(STARS_MARKER) != 1 or '</defs>' not in svg:
        sys.exit('Lo stemma base non ha la struttura attesa (pattern stelle / defs).')
    svg = svg.replace('</defs>', GRADS + '</defs>', 1)
    svg = svg.replace(STARS_MARKER, stones_group(stones) + '\n' + STARS_MARKER, 1)

    out = args.out or args.sgf.rsplit('.', 1)[0] + '_stemma.svg'
    open(out, 'w', encoding='utf-8').write(svg)
    print(f'OK -> {out}  ({len(stones)} pietre: {nb} nere, {nw} bianche)')


if __name__ == '__main__':
    main()
