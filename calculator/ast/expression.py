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
from calculator.ast.node import Node    # Used for inheritance.

################################### CLASSES ####################################

class Expression(Node):
    """
    An expression represents a non-terminal node in the AST. For instance, an
    expression could be "a + b". An expression always has two children.
    """

    def __init__(self, symbol, left_child, right_child):
        """
        Constructor of the Expression Node.

        Arguments
        =========
         - symbol: The string in the original source code from which the token
            was built.
         - left_child: The first operand in this expression, should inherit from
            Node.
         - right_child: The second operand of this expression, should inherit
            from Node.
        """
        # Calling the parent constructor.
        super(Expression, self).__init__(symbol)
        # Storing the other arguments.
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        """
        String representation of the Expression Node.
        """
        return f"({self.left_child} {self.symbol} {self.right_child})"

################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
