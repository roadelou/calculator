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
from calculator import MathLexer    # Used to parse the source before lexing it.
from calculator import MathParser   # The parser we want to test.


# Internal imports 
# Your imports within this package go here 

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def test_parser():
    """
    Simple test for the parser.
    """
    # Creating a the source code.
    source_code = "4 - (9+ 5  -6) *7-3"

    # Creating the lexer.
    lexer = MathLexer()
    # Tokenizing the source code.
    tokens = lexer.tokenize(source_code)

    # Creating the Parser.
    parser = MathParser()
    # Building the abstract syntax tree.
    ast = parser.parse(tokens)

    # Printing the parsed expressions.
    print(ast)
    # Uncomment to see the the parsed code.
    # assert False

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
