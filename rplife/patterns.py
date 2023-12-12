from dataclasses import dataclass

@dataclass
class Pattern:
    """Handles the game's patterns

    Handles the game's patterns.

    Attributes:
        name : str
            the pattern’s name.
        alive_cells: set[tuple[int, int]]
            a set of two-value tuples, giving the living cells in a pattern. A tuple represents the coordinates 
            of an alive cell in a grid. Set operations are used to determine the cells that will be alive in 
            the next generation (step/tick) during a game.
    """
    name: str
    alive_cells: set[tuple[int, int]]