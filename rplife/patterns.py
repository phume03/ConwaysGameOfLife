from dataclasses import dataclass
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

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

    Methods:
        from_toml(cls, name, toml_data):
            this is a class method, which is how to provide an alternative constructor in python classes. It is 
            initiated by the @classmethod decorator. The function receives the current class as its first 
            argument (cls), the pattern's name as the second argument, and some TOML data as the third argument. 
            The method will create and return an instance of the class passed in using the cls argument. The new
            class has the passed in parameters set as its attributes; the .alive_cells are generated using a set 
            comprehension, whereby a set of tuples is created from the list of lists that is passed in from the 
            TOML file.

        get_pattern(name, filename=PATTERNS_FILE):
            this method loads a named pattern from a TOML file. The function receives the pattern name as a
            string, and the name of the file to load the patterns from. It selects the named/labelled dictionary
            data from a TOML file, parses the data through from_toml along with it's name, and returns the 
            pattern-class instance with the TOML data loaded.

        get_all_patterns(filename=PATTERNS_FILE):
            this method loads all the patterns from a TOML file. The function receives the name of the file to 
            load the patterns from. It chooses all pattern data, and parses each data item through from_toml
            along with it's name, and returns an array of the pattern-class instances with the TOML data loaded.
    """
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls: object, name: str, toml_data: [[int, int]]):
        """an alternative constructor for the Pattern class, used to extract and format TOML data from file

        Parameters
        ----------
       cls : Pattern
            the current class

       name : str
            the name of the pattern

       toml_data : [[int, int]]
            the toml data as an array of array integer pairs                        

        Returns
        -------
        pattern : Pattern
            a named class representing the TOML data
        """
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )
    
    def get_pattern(name, filename=PATTERNS_FILE):
        """load the named pattern from the TOML file

        Parameters
        ----------
       name : str
            the name of the pattern

       filename : str
            the toml data file to read from

        Returns
        -------
        pattern : Pattern
            a named/labelled pattern-class representing the TOML data
        """        
        data = tomllib.loads(filename.read_text(encoding="utf-8"))
        return Pattern.from_toml(name, toml_data=data[name])
    
    def get_all_patterns(filename=PATTERNS_FILE):
        """load all the patterns from the TOML file

        Parameters
        ----------
       filename : str
            the toml data file to read from

        Returns
        -------
        array : Pattern-array
            the array equivalent of the patterns in the toml data file, each array entry is an instance of the pattern class
        """         
        data = tomllib.loads(filename.read_text(encoding="utf-8"))
        return [
            Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
        ]    