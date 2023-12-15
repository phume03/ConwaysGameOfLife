import collections
from rplife.patterns import Pattern

ALIVE = "♥"
DEAD = "‧"

class LifeGrid:
    """This is the board or grid for the rplife game.

    This is the board or grid for the rplife game. This will take care of evolving the grid to the next 
    generation and providing a string representation of the grid for print out to the CLI.

    Attributes:
        pattern : Pattern
            a pattern

    Methods:
        __init__(self, pattern):
            rplife grid initializer
    
        evolve(self):
            will check the currently alive cells and their neighbours to determine which cells should be alive in the next generation
        
        as_string(self, bbox):
            a way to represent the grid as a string
        
        __str__(self):
            a way to represent the containing object in a user-friendly manner
    """
    pattern: Pattern

    def __init__(self, pattern: Pattern):
        """RPLife grid initializer.

        Parameters
        ----------
        pattern : pattern
            an instance of a pattern

        Returns
        -------
        none

        """
        self.pattern = pattern
        pass

    def evolve(self):
        """will check the currently alive cells and their neighbours to determine which cells should be alive in the next generation. The rules for how cells evolve are:
            * Alive cells die if living neighbors less than 2 (underpopulation) or more than 3  (overpopulation).
            * Alive cells stay alive if living neighbors equals 2 or 3.
            * Dead cells become alive (reproduction) if living neighbors equals 3.
        
        How can you check the neighbors of a given living cell? Consider the following algorithm:
            For (0, 0), add (-1, -1) to (1, 1) value by value.
            For (0, 1), add (-1, 0) to (1, 1) value by value.
            For (0, 2), add (-1, 1) to (1, 1) value by value.
            For (1, 0), add (0, -1) to (1, 1) value by value.
            For (1, 1), skip as this is the initial cell.
            For (1, 2), add (0, 1) to (1, 1) value by value.
            For (2, 0), add (1, -1) to (1, 1) value by value.
            For (2, 1), add (1, 0) to (1, 1) value by value.
            For (2, 2), add (1, 1) to (1, 1) value by value.


        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells # python intersection

        """
        alive_set = {}
        for cell, num in num_neighbors.items():
            if num >= 2 and num <=3 or if num==2 or num==3:
                alive_set.add(cell)
        stay_alive = alive_set.intersection(self.pattern.alive_cells)         
        """
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells # set difference
        """
        dead_set = {}
        for cell, num in num_neighbors.items():
            if num == 3:
                dead_set.add(cell)
        come_alive = dead_set.difference(self.pattern.alive_cells)
        """

        self.pattern.alive_cells = stay_alive | come_alive # python union
        """
        _alive_cells = stay_alive.union(come_alive)
        self.pattern.alive_cells = _alive_cells
        """

    def as_string(self, bbox):
        """"a way to represent the grid as a string.

        The LifeGrid can be represented as a String to be displayed to your screen. The two constants, ALIVE 
        and DEAD hold the characters that will represent the alive and dead cells on the grid. The name of the
        pattern is printed to screen, centered over the grid’s width.

        Parameters
        ----------
        bbox : bbox
            a bounding box for the life grid, it will define which part of the grid you display in your terminal window

        Returns
        -------
        lifegrid : str
            a string representation of the grid

        """
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)
    
    def __str__(self):
        """a way to represent the containing object in a user-friendly manner. Similar to java's toString method.
        
        Parameters
        ----------
        none

        Returns
        -------
        pattern : str
            a formatted string of the pattern and its associated data of living cells. 
        """
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )