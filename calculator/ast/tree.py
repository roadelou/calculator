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
from calculator.ast.node import Node    # Used for composition
from calculator.ast.number import Node    # Used for downcast
from calculator.ast.expression import Node    # Used for downcast

################################### CLASSES ####################################

class Tree:
    """
    The abstract syntac tree (AST) built from the source code.
    """

    def __init__(self, head):
        """
        Constructor of the Tree class.

        Arguments
        =========
         - head: The topmost Node in the AST.
        """
        # Storing the arguments.
        self.head = head

    def __repr__(self):
        """
        String representation of the AST.
        """
        # We print the nodes recursively.
        return str(self.head)

################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
