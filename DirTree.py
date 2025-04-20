"""DirTree.py

Author: James Buntwal (James@Buntwal.com)

Description: 

    Creates a directory tree diagram

    To run for a specific filepath, in a terminal window run:

    >>> python DirTree.py '/desired/file/path'
    or
    >>> python -m DirTree '/desired/file/path'

    To run for the current working directory of the terminal window (add python file to path or to CWD) run:

    >>> python DirTree.py
    or
    >>> python -m DirTree

    To save output to text file use: '>' suffix. In a terminal window run:
    >>> python DirTree.py '/desired/file/path' > output.txt
    or 
    >>> python -m DirTree '/desired/file/path' > output.txt

"""

# Imports
import pathlib
import argparse


# Tab level 
def TabLevel(  lvl : int,
               ws : int = 4,
               h : int = 3):
    """
    Args:
        lvl = tab level (branch depth)
        ws  = white space in between tab levels
        h   = number of hyphens in final tab level

    Returns:
        a single tree branch with tabbing 
        that corresponds to the input level.

    >>> tab_level(2, 4, 3)
    '|    |    |--- '
    """
    return f"{('|'+' '*ws)*lvl}|{'-'*h} "


def PrintTree(  path    : pathlib.Path  ,
                lvl     : int           = 0):
    """
    Args:
        path = filepath of current DirTree branch
        lvl = tab level of current branch
    """

    # Print current level
    print(TabLevel(lvl), path.name)

    # Walk through child paths
    for child in path.iterdir():

        # If child path is a directory: go down a level
        if child.is_dir():
            PrintTree(child, lvl+1)
        
        # If child path is a file: print the branch
        elif child.is_file():
            print(TabLevel(lvl+1), child.name)

        


if __name__ == "__main__":

    # Instantiate Argument parser
    ParserObject = argparse.ArgumentParser()
    
    # Add path argument to parser
    ParserObject.add_argument( 'path',
                                nargs = '?', # 0 or 1 arguments
                                help = "Root folder of the diagram.",
                                default = f"{pathlib.Path.cwd()}" # Use CWD as default
                                )

    # Parse filepath and immediately convert str->pathlib.Path
    path = pathlib.Path(
        ParserObject
        .parse_args()
        .path
        )

    # Recurse through directory printing each branch
    PrintTree(path)

