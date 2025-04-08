Slither
=======
_A movement from Python to APL_

Hackr.io offers a portfolio of Python projects by Robert Johns: [40+ Python Projects + Source Code | Beginner to Advanced](https://hackr.io/blog/python-projects). 

Slither takes some of these projects and translates the solutions from Python into APL, first minimally, keeping the APL code close to to the Python, then in ‘APL-literate’ form, demonstrating a more array-oriented solution. 

![Snake and apple](forbidden-fruit.jpg)

Slither offers 

-   practice examples to study for Pythonistas learning APL
-   equivalent Python and APL programs in which to compare the two languages
-   insights from porting the code to APL, mapped back to improve the original Python
-   reflections on good coding practices, in Python and APL


APL solutions
-------------
The APL code can be loaded into a workspace, with its parts nested into namespaces.
For example, either:
```apl
]LINK.Create # /path/to/slither  ⍝ load into the workspace root
]LINK.Create   /path/to/slither  ⍝ load into #.slither
```

Certain functions, such as `input`, appear in several solutions. 
They have been abstracted into the `utilities` folder.

Examples are coded in Dyalog APL Version 20.0.


Contents
--------

-   [Projects for Beginners](beginners/)
    -   [Number Guessing](beginners/numguess/)
    -   [Rock Paper Scissors](beginners/rockpaper/)
-   [Games](games/)
    -   [Tic-Tac-Toe](games/tictactoe/)


Contribute
----------
Exercise caution when comparing APL and Python solutions.
Many of the originals are written as exercises for beginners and refrain from Python language features that might yield more of the terseness APL programmers aspire to.

Feel free to contribute a more advanced Python version, but leave the originals exactly as scraped from the Web.

Also feel free to contribute further examples, either from the Hackr.io article or elsewhere.
For these, prefer programs that demonstrate APL features not otherwise represented here.

Contact the repo owner at sjt@lambentechnology.com if you wish to discuss a candidate.