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
from calculator import MathLexer    # The lexer that we want to test.


# Internal imports 
# Your imports within this package go here 

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def test_lexer():
    """
    Tests the MathLexer on some simple example.
    """
    # We start by building a lexer.
    lexer = MathLexer()
    # We prepaer some source code.
    source_code = "2 - (4 + 8.9  )* 2"
    # We perform the tokenization.
    tokens = lexer.tokenize(source_code)
    # We print the tokens found, only displayed if the test fails.
    for token in tokens:
        print(token)
    # Uncomment to see the output.
    # assert False

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
