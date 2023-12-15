import sys

from rplife import views
from rplife.patterns import Pattern
from rplife.cli import get_command_line_args
"""The container for the entry-point to the rplife application

This is a container for the entry-point to the RPLife application.

Attributes:
    none

Methods:
    main():
        starts the execution of the rplife program

    _show_pattern(View, pattern, args):
        a helper function to display the patterns for rplife

"""

def main():
    """starts the execution of rplife application

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        
    args = get_command_line_args()
    View = getattr(views, args.view)
    if args.all:
        for pattern in Pattern.get_all_patterns():
            _show_pattern(View, 
                pattern, 
                args
            )
            pass
        pass
    else:
        _show_pattern(
            View,
            Pattern.get_pattern(name=args.pattern),
            args
        )
        pass
    pass

def _show_pattern(View, pattern: Pattern, args):
    """a helper function to display the patterns for rplife.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        
    try:
        View(pattern = pattern, 
            gen = args.gen, 
            frame_rate = args.fps
        ).show()
    except Exception as error:
        print(error, file = sys.stderr)

    pass

if __name__ == "__main__":
    main()
    pass