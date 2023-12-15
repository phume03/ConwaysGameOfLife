import argparse
from rplife import __version__, views
from rplife.patterns import Pattern
"""
This allows the rplife application to run in the command line interface (cli).

This is an implementation of an interface that will allow users of rplife to interact 
with the application in the command line. They should be able to run the game with 
different input parameters, including; life patterns, number of evolutions, frames per
second, etc. It makes use of the argparse module from the standard library.

Attributes:

Methods:
    get_command_line_args():
        this function instantiates argparser
"""

def get_command_line_args():
    """this function instantiates argparser
    
    This function instantiates argparser, and gives it basic information 
    about the application. Then, it prepares the user defined options for
    the command line interface program.

    Parameters
    ----------
    none

    Returns
    -------
    the parsed command line args as a namespace/key-value pair object
    """
        
    parser = argparse.ArgumentParser(
        prog = "rplife",
        description = "Conway's Game of Life in your terminal.",
    )

    parser.add_argument("--version",
        action = "version",
        version = f"%(prog)s v{__version__}"
    )
    parser.add_argument("-p",
        "--pattern",
        choices = [pat.name for pat in Pattern.get_all_patterns()],
        default = "Blinker",
        help = "get a pattern for the Game of Life (default: %(default)s)",
    )
    parser.add_argument("-a",
        "--all",
        action = "store_true",
        help = "show all available patterns in a sequence.",
    )
    parser.add_argument("-v",
        "--view",
        choices = views.__all__,
        default = "CursesView",
        help = "display the LifeGrid in a specific view (default: %(default)s)",
    )
    parser.add_argument("-g",
        "--gen",
        metavar = "NUM_GENERATIONS",
        type = int,
        default = 10,
        help = "number of generations (default: %(default)s)",
    )
    parser.add_argument("-f",
        "--fps",
        metavar = "FRAMES_PER_SECOND",
        type = int,
        default = 7,
        help = "frames per second (default: %(default)s)",
    )
    
    return parser.parse_args()