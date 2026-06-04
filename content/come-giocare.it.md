---
title: "Introduzione al Go"
date: 2026-06-04
---

Il **Go** (囲碁 in giapponese, 围棋 _wéiqí_ in cinese, 바둑 _baduk_ in coreano) è un
gioco di strategia per due giocatori. Partendo dalla griglia vuota, i due competono
per disporre le pietre in modo da **massimizzare la presenza delle proprie pietre e
lo spazio che esse delimitano** — lo spazio vuoto raggiungibile soltanto dal proprio
colore.

## Le origini

Le prime fonti storiche che fanno riferimento al gioco del Go sono tre opere
confuciane databili tra il IV e il III secolo a.C.: lo *Zuo Zhuan*, il libro IV del
*Mencio* e il libro XVII dei *Dialoghi* di Confucio. I primi riferimenti sono
critici — il *Mencio* annovera chi indulge nel Go tra i comportamenti non filiali —
ma sotto l'influenza neoconfuciana della dinastia Song questa percezione cambia: il
classico in tredici capitoli *Qijing Shisanpian* (circa 1050 d.C.) legge il gioco
alla luce delle teorie taoiste e di Sun Tzu. Da allora la pratica del Go è
considerata una via di accrescimento morale e intellettuale. Per la loro
semplicità, le regole essenziali del gioco sono rimaste immutate nei secoli.

## Le regole

Il Go si gioca sul **goban**, il tavoliere — di norma in legno — su cui è tracciata
una griglia di linee. Non ci sono caselle: si gioca sugli **incroci** delle linee.
Il formato standard è di **19×19 linee** (altri sono possibili — ai principianti si
consiglia 9×9 o 13×13). Due giocatori, a turno, dispongono uno le **pietre bianche**,
l'altro le **pietre nere**.

1. **A turno.** Iniziando dalla griglia vuota, **il Nero muove per primo**; poi ci
   si alterna. Una pietra posata non si sposta più.
2. **Gruppi e libertà.** Le pietre dello stesso colore connesse ortogonalmente
   formano un **gruppo**, che condivide gli spazi vuoti adiacenti: le sue
   **libertà**. Anche una pietra singola è un gruppo.
3. **Cattura.** Alla fine di ogni turno, un gruppo rimasto **senza libertà** viene
   rimosso dal tavoliere, perché *catturato* dalle pietre avversarie. Non si può
   giocare in un punto dove la propria pietra non avrebbe libertà — a meno che
   quella mossa non catturi prima un gruppo nemico.
4. **Territorio.** Vince chi, alla fine, controlla più punti: si contano le
   intersezioni vuote circondate dal proprio colore, più le pietre catturate.

{{< goban caption="La pietra bianca ha una sola libertà, il punto A: se il Nero gioca in A, la cattura e la toglie dal tavoliere." >}}
.X.
XOA
.X.
{{< /goban >}}

## Vita e morte: la vita incondizionata

Dalle regole nasce il cuore strategico del Go. Un gruppo è al sicuro quando è
**vivo**, cioè non più catturabile. La forma fondamentale è quella dei **due occhi**:
due spazi vuoti interni separati. L'avversario non può riempirli entrambi — per
occupare il secondo dovrebbe giocare una pietra priva di libertà, mossa proibita —
e così il gruppo resta **incondizionatamente vivo**: a qualsiasi attacco il
difensore può sempre rispondere conservando due libertà interne in cui il nemico
non può entrare.

{{< goban caption="Due occhi (A e B): il gruppo bianco è incondizionatamente vivo. Il Nero non può giocare né in A né in B, perché quella pietra sarebbe priva di libertà." >}}
OOOOO
OAOBO
OOOOO
{{< /goban >}}

A volte i due occhi non ci sono ancora, ma sono **garantiti**. È il principio del
*miai*: quando esistono due punti chiave e l'avversario può occuparne soltanto uno,
l'altro resta sempre a disposizione del difensore. Nella fila di quattro qui sotto i
punti decisivi sono **B** e **C**: se il Nero gioca in uno, il Bianco risponde
nell'altro e si fa due occhi — perciò il gruppo è già vivo.

{{< goban caption="Fila di quattro (A–D) sul bordo: il Bianco è vivo. I punti chiave sono B e C; il Nero può occuparne solo uno, il Bianco prende l'altro e ottiene due occhi." >}}
OABCDO
OOOOOO
{{< /goban >}}

Riconoscere quando un gruppo è vivo, morto, o ancora in bilico è l'arte della *vita
e morte* (*tsumego*), il primo grande passo verso il gioco vero.

## Regole semplici, possibilità sterminate

Poche regole, complessità immensa. Le posizioni legali sul 19×19 sono circa
**2,08 × 10¹⁷⁰**, e il numero di partite possibili supera ogni intuizione. Pur
essendo un gioco a **informazione perfetta** — in teoria esiste una mossa ottima in
ogni posizione — l'albero di gioco è così profondo (circa 200 mosse, con circa 200
scelte per mossa) che risolverlo per via ricorsiva sul 19×19 **non è fattibile**. È
per questo che il Go è citato come esempio di *comportamento emergente*: da regole
elementari emergono forme di una ricchezza inesauribile.

## Il Go e la mente

Per la sua combinazione di **regole minime e complessità sterminata**, il Go è un
*microcosmo controllato* ideale per studiare la mente. È il ruolo che i giochi hanno
avuto a lungo nelle scienze cognitive e nell'intelligenza artificiale: gli scacchi
furono per decenni definiti la «**Drosophila dell'IA**» — l'organismo-modello su cui
fare esperimenti, come il moscerino della frutta per la genetica (l'espressione
risale agli anni '60; sulla sua fortuna e i suoi limiti, Ensmenger, 2012). Il Go,
più vasto e sfuggente, è stato proposto come banco di prova ancora più impegnativo
(Burmeister & Wiles, 1995) e come **dominio fecondo per la psicologia cognitiva**,
dove indagare memoria, apprendimento implicito e percettivo, *problem solving* e
attenzione (Burmeister, 2000).

Lo stesso Herbert Simon, dopo aver indagato il *problem solving* umano (Newell &
Simon, 1972), mostrò con Chase che — come negli scacchi — il giocatore esperto non
vede pezzi isolati ma **configurazioni** (Chase & Simon, 1973): percepisce la
posizione in unità di senso, i *chunk*, e ricostruisce a memoria una partita reale
molto meglio di una disposizione casuale — un effetto studiato sul Go fin da Reitman
(1976). Da quell'intuizione nacque la *chunk theory* e, in seguito, la **template
theory** (Gobet & Simon, 1996): con l'esperienza i *chunk* si organizzano in schemi
più ampi e flessibili, i *template*, che consentono al maestro di cogliere e
memorizzare un'intera configurazione in un colpo solo. Non a caso, ai livelli più
alti si accompagnano in genere abilità **visuo-spaziali e di riconoscimento di
forme** più spiccate (Wojtasinski & Francuz, 2018).

Diventare forti, però, richiede tempo: si stimano **almeno dieci anni** di studio
strutturato per una piena maturazione. Studiando centinaia di giocatori dal
principiante al professionista, Masunaga & Horn (2000) hanno osservato che questa
crescita si accompagna allo sviluppo di **strutture cognitive specifiche del
dominio** — una memoria di lavoro ad ampio span (*Expertise Working Memory*) e un
ragionamento deduttivo dedicati al gioco (*Expertise Deductive Reasoning*) —
relativamente **indipendenti** dalle capacità cognitive generali. In altre parole:
al goban non si diventa forti solo perché si è "intelligenti"; si costruisce, mossa
dopo mossa, una mente fatta apposta per il Go.

A questo programma di ricerca, perseguito per decenni, si lega l'episodio più noto.
Il nodo del Go non è la profondità del calcolo ma la **valutazione della posizione**:
stabilire chi stia meglio, ciò che il maestro coglie per intuizione. Negli scacchi
questa valutazione si poteva in larga parte **progettare a mano** e abbinare a una
ricerca profonda — è la via di Deep Blue (1997) — mentre nel Go si è rivelata assai
più difficile da codificare. La svolta venne dapprima dai metodi **Monte Carlo** ad
albero (anni 2000) e infine da **AlphaGo** (Silver et al., 2016), che alla ricerca
affiancò due **reti neurali profonde** apprese da partite umane e dal gioco contro
sé stesso: una *policy network* che propone le mosse plausibili e una *value
network* che stima il valore di una posizione. La valutazione che nell'esperto umano
poggia sul riconoscimento di *chunk* e *template* è diventata, nella macchina, una
funzione **appresa** anziché scritta a mano: una convergenza — non un'identità — che
riporta il Go al centro delle scienze cognitive.

## Riferimenti

Le opere citate in questa pagina, per chi vuole approfondire:

- Shotwell, P. (2008). *The Game of Go: Speculations on its Origins and Symbolism in Ancient China*. American Go Association. [PDF](http://www.usgo.org/files/bh_library/originsofgo.pdf)
- Gosset, D. (2010). *Weiqi: A Symbol of the Chinese Experience*. Chinese American Forum. [PDF](http://caforumonline.net/CAFHandlerPDF.ashx?ID=360)
- Benson, D. (1976). *Life in the Game of Go*. Information Sciences, 10, 17–29. [PDF](http://webdocs.cs.ualberta.ca/~games/go/seminar/2002/020717/benson.pdf)
- Tromp, J., & Farnebäck, G. (2016). *Combinatorics of Go*. [PDF](https://tromp.github.io/go/gostate.pdf)
- Walraet, M., & Tromp, J. (2016). *A Googolplex of Go Games*. [PDF](https://matthieuw.github.io/go-games-number/AGooglplexOfGoGames.pdf)
- Allis, L. V. (1994). *Searching for Solutions in Games and Artificial Intelligence* (tesi di dottorato). [PDF](http://fragrieu.free.fr/SearchingForSolutions.pdf)
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
- **Sgaravatti, N.** *Costruzione e validazione di uno spazio di apprendimento nel gioco del Go*. Università degli Studi di Padova. [Archivio tesi UniPD](https://thesis.unipd.it/handle/20.500.12608/30402) — da cui è tratto l'impianto di questa pagina.

## Dove imparare e giocare online

- **[Online-Go (OGS)](https://online-go.com/)** — gioca e impara gratis nel browser.
- **[Sensei's Library](https://senseis.xmp.net/)** — la grande enciclopedia del Go (in inglese).
- **[Federazione Italiana Giuoco Go (FIGG)](https://www.figg.org/)** — la federazione
  nazionale: regole, tornei e circoli in Italia.
- **App per smartphone** come _BadukPop_ o _Go Free_ per esercitarti con i problemi.

## Il modo migliore? Vieni a trovarci

Imparare a giocare davanti a un goban vero, con qualcuno che ti guida, vale più di
mille tutorial. Al circolo troverai sempre qualcuno pronto a insegnarti le basi.

👉 Scopri [dove e quando ci incontriamo](/it/contatti/).
