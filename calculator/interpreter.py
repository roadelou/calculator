#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-05
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
# Your imports from the standard library go here 


# External imports 
# Your imports from other packages go here 


# Internal imports 
from calculator.ast import Tree, Node, Number, Expression   # Used for downcasts.

################################### CLASSES ####################################

class MathInterpreter:
    """
    Simple interpreter for the mathematical expressions we have built.
    """
    # Constructor is the same as Object for now.
    
    def run(self, ast: Tree) -> float:
        """
        Performs the computation described by the provided AST and returns its
        result.

        Arguments
        =========
         - ast: The AST describing the computation we should perform.

        Returns
        =======
        The floating point result of the computation.
        """
        # We recursively perform the computations described by the AST, starting
        # from its head.
        return recursive_run(ast.head)

################################## FUNCTIONS ###################################

def recursive_run(node: Node) -> float:
    """
    Recursively runs and returns the result of the computation described in the
    provided Node of the Abstract syntax tree.

    Arguments
    =========
     - node: The Node of the AST to recursively interpret,

    Returns
    =======
    The floating point result of the computation.
    """
    # The first thing is to downcast the node to its real type.
    if isinstance(node, Number):
        # The node is just a number, we may return it.
        return node.value
    else:   # isinstance(node, Expression)
        # The node is an expression, we have to recursively compute the left and
        # right side of the expression.
        left_side = recursive_run(node.left_child)
        right_side = recursive_run(node.right_child)
        # Then we look at the symbol in our Expression to see which computation
        # should be performed.
        if node.symbol == "+":
            return left_side + right_side
        elif node.symbol == "-":
            return left_side - right_side
        elif node.symbol == "*":
            return left_side * right_side
        elif node.symbol == "/":
            return left_side / right_side

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
