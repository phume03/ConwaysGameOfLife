"""
Conway's Game of Life is a game about the evolution of cells in a life grid.


Conway's Game of Life (also known simply as Life or rplife), is a cellular automaton devised by the British 
mathematician John Horton Conway in 1970. It is a zero-player game whereby gameplay is determined by the initial 
state, or seed. After the game starts, it requires no further input from an external user. 


Modules:
    __main__.py - starts the execution of rplife as a part of the __init__ entry-point.
    cli.py      - contains the command-line interface for the game.
    grid.py     - provides the LifeGrid implementation.
    patterns.py - handle the game’s patterns.
    views.py    - implements curses to display the life grid and its evolution.

"""
__version__ = "1.0.0"