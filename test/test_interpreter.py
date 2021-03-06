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
from calculator import MathInterpreter  # The interpreter we want to test.
from calculator.ast import Tree, Number, Expression # Used to build the test AST.


# Internal imports 
# Your imports within this package go here 

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def test_interpreter():
    """
    Simple test for the interpreter, without using lexer and parser.
    """
    # We start by building the AST for "1 + 3.4 - (6 * 0.22) / 4"
    number_0 = Number("1")
    number_1 = Number("3.4")
    number_2 = Number("6")
    number_3 = Number("0.22")
    number_4 = Number("4")

    expression_0 = Expression("+", number_0, number_1)
    expression_1 = Expression("*", number_2, number_3)
    expression_2 = Expression("/", expression_1, number_4)
    expression_3 = Expression("-", expression_0, expression_2)

    tree = Tree(expression_3)

    # We build the interpreter.
    interpreter = MathInterpreter()
    # We run the computation from the AST.
    interpreter_result = interpreter.run(tree)
    # We also run the computation in Python.
    reference_result = 1 + 3.4 - (6*0.22) /4
    # We assert that the resuts are close enough.
    assert abs(interpreter_result - reference_result) < 0.001

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
