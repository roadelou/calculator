#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-06
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class Node:
    """
    Abstract class representing a node in the abstract syntax tree.
    """

    def __init__(self, symbol):
        """
        Constructor to set some fields common to all the Nodes.

        Arguments
        =========
         - symbol: The string from which this Node was originaly constructed from.
        """
        # Storing the argument values.
        self.symbol = symbol


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
