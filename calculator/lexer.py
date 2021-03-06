#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-05
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import logging  # Used to print error messages, but keep trying to parse the source


# External imports
from sly import Lexer  # Lexer implementation


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class MathLexer(Lexer):
    """
    Lexer for basic mathematical operations. Uses the PLY project.
    """

    # Tuple of tokens used in mathematical expressions.
    tokens = {"NUMBER", "PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN"}

    # We ignore tabs and spaces.
    ignore = " \t"

    # Simple tokens are matched using regular expressions.
    PLUS = r"\+"
    MINUS = r"-"
    TIMES = r"\*"
    DIVIDE = r"/"
    LPAREN = r"\("
    RPAREN = r"\)"
    NUMBER = r"\d*\.\d+|\d+"
    # Above we have defined a number as something that:
    # - either starts with 0 or 1 of "+" or "-", then has 0 or more digits
    #   and a "." than 1 or more digits.
    # - or something that starts with 0 or 1 of "+" or "-", then has 1 or
    #   more digits.

    # Defining a newline rule as advised by the documentation.
    @_(r"\n+")
    def t_newline(self, token):
        # We increase the line count for each line matched.
        token.lexer.lineno += len(token.value)

    # Error handling rule, as advised by the documentation.
    def t_error(self, token):
        # Logging an error message.
        loggin.error(f"Illegal characters {token.value}")
        # Skipping the invalid tokens to still try to read the rest of the source code.
        token.lexer.skip(len(token.value))


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
