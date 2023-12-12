from rplife import grid, patterns

"""RPLife basic examples.

These are RPLife examples. The script imports some rplife modules, like: the grid and pattern. It creates named 
instances of pattern. Then, it creates a LifeGrid object using the desired instance which it then prints out
in different states from initialization and so on.

The first example is the blinker pattern. With this pattern if you evolve the grid an even number of times, the 
grid produces the same set of live cells that were used as the initial seed for the game. This is because the 
Blinker pattern is an oscillator pattern that evolves like this: the Blinker pattern displays three horizontal 
alive cells in one generation and three vertical alive cells in the next generation.
"""
blinker = patterns.Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})
grid = grid.LifeGrid(blinker)
print(grid)

grid.evolve()
print(grid)

grid.evolve()
print(grid)

# It is at initial state
print(grid.as_string((0, 0, 5, 5)))

grid.evolve()
print(grid.as_string((0, 0, 5, 5)))

grid.evolve()
print(grid.as_string((0, 0, 5, 5)))

