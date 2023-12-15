import curses
from time import sleep
from rplife.grid import LifeGrid
from rplife.patterns import Pattern

__all__ = ["CursesView"]

class CursesView:
    """Game of Life Text-Based User Interface (TUI) to display the game to screen

    This class implements the curses library inorder to display the game of life's
    text-based user interface (TUI) to the screen. 

    Attributes:
        none

    Methods:
        __init__(self, pattern, gen=10, frame_rate=7, bbox=(0, 0, 20, 20)):
            view class initializer. It takes pattern, gen, frame_rate, and bbox as
            arguments. Pattern represents the loaded life pattern, gen represents
            number of generations/ticks/evolutions of your game, frame_rate is the 
            frames per second and represents the time between two consecutive
            generations, and bbox is the bounding box which represents the part of
            game to be displayed to screen.

        show():
            this function displays the LifeGrid to the screen.

        _draw():
            this function displays the consecutive generations of cells.

    """
    def __init__(self, pattern: Pattern, gen=10, frame_rate=7, bbox=(0, 0, 20, 20)):
        """view class initializer

        Parameters:
        ----------
        pattern : object
            the pattern to be displayed to screen

        gen : int
            number of ticks/simulations/generations of the game to evolve through. Default is 10

        frame_rate : int
            the amount of time to pause between evolution displays, high numbers will make the display 
            too slow, and low numbers will switch out too fast. Default is 7

        bbox : tuple(int, int, int, int)
            bounding box/frame for the game/grid


        Returns:
        -------
        none

        """
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox
        pass

    def show(self):
        """this function initializes a curses screen and then displays 
        the LifeGrid to the screen.

        Parameters:
        ----------
        none

        Returns:
        -------
        implicitly returns a curses screen for display.

        """
        curses.initscr()        
        curses.wrapper(self._draw)        
        pass

    def _draw(self, screen):
        """this function displays the consecutive generations of cells.

        Parameters:
        ----------
        
        screen: CursesPanel
            this is a curses window

        Returns:
        -------
        none

        """ 
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0,0,current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"ERROR: Terminal too small for pattern'{self.pattern.name}'"
            )
        
        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0,0,current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1/self.frame_rate)
            pass
        
        pass