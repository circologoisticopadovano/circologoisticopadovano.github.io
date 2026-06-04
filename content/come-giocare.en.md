---
title: "Introduction to Go"
slug: "how-to-play"
date: 2026-06-04
---

**Go** (囲碁 in Japanese, 围棋 _wéiqí_ in Chinese, 바둑 _baduk_ in Korean) is a game
of strategy for two players. Starting from the empty grid, the two compete to place
their stones so as to **maximise the presence of their own stones and the space
those stones enclose** — the empty space reachable only by their own colour.

## Origins

The earliest historical sources mentioning Go are three Confucian works datable
between the 4th and 3rd centuries BC: the *Zuo Zhuan*, Book IV of the *Mencius* and
Book XVII of Confucius' *Analects*. The first references are critical — the
*Mencius* lists indulging in Go among unfilial behaviours — but under the
Neo-Confucian influence of the Song dynasty this perception changes: the
thirteen-chapter classic *Qijing Shisanpian* (c. 1050 AD) reads the game in the
light of Taoist thought and of Sun Tzu. Ever since, Go has been seen as a path of
moral and intellectual growth. Owing to their simplicity, the essential rules of
the game have remained unchanged through the centuries.

## The rules

Go is played on the **goban**, the board — usually wooden — on which a grid of
lines is drawn. There are no squares: you play on the **intersections** of the
lines. The standard format is **19×19 lines** (other sizes are possible — beginners
are advised to start on 9×9 or 13×13). Two players take turns placing one the
**white stones**, the other the **black stones**.

1. **In turn.** Starting from the empty grid, **Black moves first**; then players
   alternate. A placed stone never moves again.
2. **Groups and liberties.** Stones of the same colour connected orthogonally form
   a **group**, which shares the adjacent empty points: its **liberties**. A single
   stone is itself a group.
3. **Capture.** At the end of each turn, a group left **with no liberties** is
   removed from the board, *captured* by the opposing stones. You may not play on a
   point where your own stone would have no liberty — unless that move first
   captures an enemy group.
4. **Territory.** Whoever controls more points wins: you count the empty
   intersections surrounded by your colour, plus the stones you captured.

{{< goban caption="The white stone has a single liberty, point A: if Black plays at A, it captures the stone and removes it from the board." >}}
.X.
XOA
.X.
{{< /goban >}}

## Life and death: unconditional life

The strategic heart of Go grows out of these rules. A group is safe when it is
**alive**, that is, no longer capturable. The fundamental shape is that of **two
eyes**: two separate internal empty points. The opponent cannot fill both — to take
the second they would have to play a stone with no liberty, a forbidden move — and
so the group is **unconditionally alive**: to any attack the defender can always
reply while keeping two internal liberties the enemy cannot enter.

{{< goban caption="Two eyes (A and B): the white group is unconditionally alive. Black can play neither at A nor at B, because such a stone would have no liberty." >}}
OOOOO
OAOBO
OOOOO
{{< /goban >}}

Sometimes the two eyes are not there yet, but are **guaranteed**. This is the
*miai* principle: when two key points exist and the opponent can occupy only one of
them, the other always stays available to the defender. In the straight four below
the decisive points are **B** and **C**: if Black plays one, White answers on the
other and makes two eyes — so the group is already alive.

{{< goban caption="A straight four (A–D) on the edge: White is alive. The key points are B and C; Black can occupy only one, White takes the other and gets two eyes." >}}
OABCDO
OOOOOO
{{< /goban >}}

Recognising when a group is alive, dead, or still in the balance is the art of
*life and death* (*tsumego*), the first great step towards real play.

## Simple rules, boundless possibilities

Few rules, immense complexity. The legal positions on the 19×19 board number about
**2.08 × 10¹⁷⁰**, and the number of possible games defies intuition. Although Go is
a game of **perfect information** — in theory an optimal move exists in every
position — its game tree is so deep (about 200 moves, with roughly 200 choices each)
that solving it recursively on 19×19 **is not feasible**. This is why Go is cited as
an example of *emergent behaviour*: from elementary rules arise forms of
inexhaustible richness.

## Go and the mind

For its combination of **minimal rules and boundless complexity**, Go is an ideal
*controlled microcosm* for studying the mind. Games have long played this role in
cognitive science and artificial intelligence: chess was for decades called the
«**Drosophila of AI**» — the model organism to experiment on, as the fruit fly is
for genetics (the phrase dates to the 1960s; on its fortunes and limits, Ensmenger,
2012). Go, vaster and more elusive, has been proposed as an even more demanding
testbed (Burmeister & Wiles, 1995) and as a **fertile domain for cognitive
psychology** — for studying memory, implicit and perceptual learning, problem
solving and attention (Burmeister, 2000).

Herbert Simon himself, after studying human *problem solving* (Newell & Simon,
1972), showed with Chase that — as in chess — the expert player does not see
isolated pieces but **configurations** (Chase & Simon, 1973): they perceive the
position in meaningful units, *chunks*, and recall a real game far better than a
random arrangement — an effect studied in Go as early as Reitman (1976). From that
insight grew *chunk theory* and, later, **template theory** (Gobet & Simon, 1996):
with experience the chunks organise into larger, more flexible schemas, *templates*,
which let a master grasp and memorise a whole configuration at once. Fittingly,
higher-level players tend to show stronger **visuospatial and pattern-recognition
abilities** (Wojtasinski & Francuz, 2018).

Becoming strong, though, takes time: an estimated **ten years at least** of
structured study for full maturity. Studying hundreds of players from beginner to
professional, Masunaga & Horn (2000) found that this growth goes hand in hand with
the development of **domain-specific cognitive structures** — a wide-span working
memory (*Expertise Working Memory*) and a deductive reasoning dedicated to the game
(*Expertise Deductive Reasoning*) — relatively **independent** of general cognitive
ability. In other words: at the goban you do not become strong merely because you
are "intelligent"; move by move, you build a mind made for Go.

To this research programme, pursued for decades, belongs the most famous episode of
all. The crux of Go is not the depth of calculation but the **evaluation of a
position**: telling who stands better, what a master grasps by intuition. In chess
this evaluation could largely be **hand-crafted** and paired with deep search — the
path of Deep Blue (1997) — whereas in Go it proved far harder to encode. The
breakthrough came first from **Monte Carlo** tree-search methods (in the 2000s) and
finally from **AlphaGo** (Silver et al., 2016), which paired search with two **deep
neural networks** learned from human games and from self-play: a *policy network*
that proposes plausible moves and a *value network* that estimates a position's
worth. The evaluation that in the human expert rests on the recognition of *chunks*
and *templates* became, in the machine, a **learned** function rather than a
hand-written one: a convergence — not an identity — that brings Go back to the heart
of cognitive science.

## References

The works cited on this page, for those who want to go deeper:

- Shotwell, P. (2008). *The Game of Go: Speculations on its Origins and Symbolism in Ancient China*. American Go Association. [PDF](http://www.usgo.org/files/bh_library/originsofgo.pdf)
- Gosset, D. (2010). *Weiqi: A Symbol of the Chinese Experience*. Chinese American Forum. [PDF](http://caforumonline.net/CAFHandlerPDF.ashx?ID=360)
- Benson, D. (1976). *Life in the Game of Go*. Information Sciences, 10, 17–29. [PDF](http://webdocs.cs.ualberta.ca/~games/go/seminar/2002/020717/benson.pdf)
- Tromp, J., & Farnebäck, G. (2016). *Combinatorics of Go*. [PDF](https://tromp.github.io/go/gostate.pdf)
- Walraet, M., & Tromp, J. (2016). *A Googolplex of Go Games*. [PDF](https://matthieuw.github.io/go-games-number/AGooglplexOfGoGames.pdf)
- Allis, L. V. (1994). *Searching for Solutions in Games and Artificial Intelligence* (PhD thesis). [PDF](http://fragrieu.free.fr/SearchingForSolutions.pdf)
- Van der Werf, E. (2003). *Solving Go on Small Boards*. ICGA Journal, 26(2). [PDF](http://erikvanderwerf.tengen.nl/pubdown/solving_go_on_small_boards.pdf)
- Burmeister, J. M. (2000). *Studies in Human and Computer Go*. [PDF](https://staff.itee.uq.edu.au/janetw/Computer%20Go/PhD_thesis.pdf)
- Burmeister, J. M., & Wiles, J. (1995). *The Challenge of Go as a Domain for AI Research: A Comparison Between Go and Chess*. Proc. ANZIIS '95.
- Silver, D., Huang, A., Maddison, C. J., et al. (2016). *Mastering the Game of Go with Deep Neural Networks and Tree Search*. Nature, 529, 484–489. [DOI](https://doi.org/10.1038/nature16961)
- Newell, A., & Simon, H. A. (1972). *Human Problem Solving*. Prentice-Hall.
- Ensmenger, N. (2012). *Is Chess the Drosophila of Artificial Intelligence? A Social History of an Algorithm*. Social Studies of Science, 42(1), 5–30. [DOI](https://journals.sagepub.com/doi/abs/10.1177/0306312711424596)
- Masunaga, H., & Horn, J. (2000). *Characterizing Mature Human Intelligence: Expertise Development*. Learning and Individual Differences, 12, 5–33.
- Chase, W. G., & Simon, H. A. (1973). *Perception in Chess*. Cognitive Psychology, 4, 55–81.
- Reitman, J. (1976). *Deducing Memory Structures from Inter-Response Times*. Cognitive Psychology, 3, 336–356.
- Wojtasinski, M., & Francuz, P. (2018). *Expertise in the Game of Go and Levels of Visuospatial and Pattern Recognition Abilities*. [DOI](https://doi.org/10.1111/jpr.12236)
- Gobet, F., Retschitzki, J., & de Voogt, A. (2004). *Moves in Mind: The Psychology of Board Games*. [DOI](https://doi.org/10.4324/9780203503638)
- Gobet, F., & Simon, H. A. (1996). *Templates in Chess Memory: A Mechanism for Recalling Several Boards*. Cognitive Psychology, 31(1), 1–40.
- Hofstadter, D. R. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*. Basic Books.
- **Sgaravatti, N.** *Costruzione e validazione di uno spazio di apprendimento nel gioco del Go*. University of Padua. [UniPD thesis archive](https://thesis.unipd.it/handle/20.500.12608/30402) — from which this page's framework is drawn.

## Where to learn and play online

- **[Online-Go (OGS)](https://online-go.com/)** — play and learn for free in your browser.
- **[Sensei's Library](https://senseis.xmp.net/)** — the great Go encyclopedia (in English).
- **[Italian Go Federation (FIGG)](https://www.figg.org/)** — the national
  federation: rules, tournaments and clubs in Italy.
- **Smartphone apps** such as _BadukPop_ or _Go Free_ to practise with problems.

## The best way? Come and visit us

Learning to play in front of a real goban, with someone guiding you, is worth more
than a thousand tutorials. At the club you will always find someone ready to teach
you the basics.

👉 Find out [where and when we meet](/en/contact/).
