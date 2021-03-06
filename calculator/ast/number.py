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
from calculator.ast.node import Node  # Used for inheritance.

################################### CLASSES ####################################


class Number(Node):
    """
    An operand is a leaf in the AST for mathematical expressions, it binds to a
    litteral number in the source code.
    """

    def __init__(self, symbol):
        """
        Constructor of the Number Node..

        Arguments
        =========
         - symbol: The string from which this Node was originaly constructed from.
        """
        # Calling parent constructor.
        super(Number, self).__init__(symbol)
        # We also get the float value of the number from its representation.
        self.value = float(symbol)

    def __repr__(self):
        """
        String representation of the Number Node.
        """
        return self.symbol


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
