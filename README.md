# Sito del Circolo Goistico Padovano

Sito statico realizzato con [Hugo](https://gohugo.io/) e tema
[PaperMod](https://github.com/adityatelange/hugo-PaperMod), pubblicato
automaticamente su **GitHub Pages** ad ogni push sul branch `main`.

🔗 **Sito online:** https://circologoisticopadovano.github.io/

## Struttura

```
content/            # i contenuti del sito, in Markdown
  _index.md         # Home
  chi-siamo.md
  come-giocare.md
  contatti.md
  news/             # sezione News & Eventi (un file = un articolo)
hugo.toml           # configurazione del sito e menu
themes/PaperMod/    # tema grafico (git submodule)
.github/workflows/  # build & deploy automatici su GitHub Pages
```

## Modificare i contenuti

Tutti i testi sono in `content/` e si scrivono in **Markdown**. Per pubblicare
una modifica basta fare commit e push su `main`: la GitHub Action ricostruisce
il sito e lo pubblica in pochi minuti.

### Aggiungere una news

Crea un nuovo file in `content/news/`, ad esempio
`content/news/torneo-primavera.md`:

```markdown
---
title: "Torneo di primavera"
date: 2026-04-12
summary: "Breve riassunto che appare nell'elenco delle news."
---

Testo dell'articolo in Markdown...
```

> Imposta `draft: true` nel front matter per tenere un articolo come bozza non
> pubblicata.

## Sviluppo in locale (opzionale)

Richiede Hugo **extended** installato (`brew install hugo`):

```bash
git clone --recurse-submodules <url-del-repo>
cd circologoisticopadovano.github.io
hugo server -D        # anteprima su http://localhost:1313/
```

Se hai già clonato senza i submodule:

```bash
git submodule update --init --recursive
```

## Pubblicazione

Il deploy è automatico tramite GitHub Actions. **Una sola configurazione manuale**
è necessaria la prima volta: su GitHub → **Settings → Pages → Build and
deployment → Source = "GitHub Actions"**.
