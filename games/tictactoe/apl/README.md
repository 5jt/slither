Tic Tac Toe in APL
==================

> ## Personal note
>
> This project is a particular favourite of mine because, when I was at school and our math teacher
> introduced us to programming, instead of setting us conventional Computer Science problems such 
> as extended precision arithmetic, he suggested some topics and invited us to tackle what interested us.
>
> At 16, I wrote my first neural network in FORTRAN and showed it could learn its way through a network.
> To be fair, I think the network had only 6 nodes.
>
> My friend Dave wrote a program to play Tic Tac Toe, which we called Noughts And Crosses.
> He never got it to cheating, but he did manage to shut down the ‘Dragon’ and ‘Zebra’ nuclear reactors 
> and evacuate the UK Atomic Energy research station at Winfrith Newburgh in Dorset.
>
> So, in the followinng century, I am pleased to close the circle with working code.
> (Not in FORTRAN, though.)
>
> SJT

Transliterate from Python 
---------------------------

FIXME

Single player with TUI
----------------------

Set the GUI aside to start with and focus on the game logic, 
using a simple text user interface (TUI) in the REPL.

With this focus, we can get the program to play against us.
It uses a function `best` to pick a player’s best available move.

[`TttTui.aplf`](apl/TttTui.aplf)

Autoplay with DSL
-----------------

Separating the UI from the game logic left us with a DSL (domain-specific language)
we can use to get the program to play aginst itself and map starting cells to results.

The symmetry of the board should be reflected in the results:
all four corners should have the same result; as should the four midpoints.
It is not so: that shows the algorithm in `best` could be improved.

[`Auto`](apl/Auto.aplf)

Single player with HTML GUI
---------------------------

With a DSL for the game logic we replace the TUI with a GUI based on the HTML Renderer object.

[`TttHtml`](apl/TttHtml.aplf)

APL: one or two players with HTTP GUI
-------------------------------------

FIXME