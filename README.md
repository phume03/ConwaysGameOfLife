# `rplife`

[Wikipedia says that](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) **the Game of Life** (also known simply as **Life** -- **rplife**), is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game. Thus gameplay is determined by the initial state, or seed. Then, the game requires no further input. It can be said that your only interaction with the system is in the initial configuration and observing how the develops/evolves. 

CS nerds will enjoy this little bit: It is Turing complete and can simulate a universal constructor or any other Turing machine.


### Rules

The universe of the Game of Life is an infinite, 2D orthogonal grid of square cells. Each cell of every cell in this grid is in one of two possible states; alive or dead. You can also think, *populated* or *unpopulated*, in respect to "living". If you know grids, then every cell has eight neighbours, so every cell interacts with its eight neighbours. At each point in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.


## Installation

1. Create and activate a Python virtual environment. You may have to point to the entire python path depending on the version of python that you wish to run e.g. Python2, Python3, etc:

```sh
$ python3 -m venv ./venv
$ source venv/Scripts/activate
(venv) $
```

2. Install `rplife` in editable mode:

```sh
(venv) $ cd source_code_final
(venv) $ pip install -e .
```

3. If you find that a module is missing, you can run pip to install that module:

```sh
(venv) $ pip install windows-curses
(venv) $
```


## Execution

To execute `rplife`, go ahead and run the following command:

```sh
(venv) $ rplife -a
```


## Acknowledgements

Author: Real Python - Email: office@realpython.com
Editor/Learner: Phume - Email: NA

Why does it matter to acknowledge? Well, the guys at Real Python sell coursework, work you would otherwise produce at a university or other... for a fee. You are seeing this, not as a template but worked on my repo. So, I completed that work, or edited their templates. If you take anything from this work (rplife), I only care you know not to ask them why things work a particular way, it will largely be my responsibility to explain that. So, if their course changes and you feel this work misrepresents a thing or ruins your experience, it is because I will not try to keep up with them, I did it, finished, and moved on. But it might still help you to read someone else's code... legally! 

Side story: before I went to University it was like there was no source code in the wild or you had to hack to get it... what rubbish, who wants that, you might hack to get EAs Doom but not to read the source... I was cool... but as we graduated we were struck/petrified by the fear of having to read someone else's code, if you completed (wrote, proof read/checked) senior level cs-coding assignments you get me... stuff's long... your first 1000 lines of code maybe... sheesh.


## License

Distributed under the MIT license. See `LICENSE` for more information.

## Resources

* [Build Conway's Game of Life With Python](https://realpython.com/conway-game-of-life-python/)

* [Get Your Own: Python Tricks Sample Chapter](https://realpython.com/bonus/python-tricks-sample-pdf/)