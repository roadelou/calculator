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
from sly import Parser  # USed to build the parser for inheritance.


# Internal imports 
from calculator.lexer import MathLexer # Used to get the static tokens from the class.
from calculator.ast import Tree, Expression, Number # Used to build the abtract syntax tree.

################################### CLASSES ####################################

class MathParser(Parser):
    """
    Parser used to build the abstract syntax tree of the mathematical
    expressions.
    """

    # We share the tokens of the Lexer.
    tokens = MathLexer.tokens

    # We also define precedence for the rules used, so that certain operations
    # have a higher priority.
    precedence = (
        ("left", PLUS, MINUS),
        ("left", TIMES, DIVIDE),
    )

    # The final rule, which returns the abstract syntax tree from the topmost
    # Node.
    @_("expr")
    def statement(self, p):
        # Returning the AST from the top Node.
        return Tree(head=p.expr)

    # The addition rule, which sums two expressions and returns a new one.
    @_("expr PLUS expr")
    def expr(self, p):
        # Building a new Node for this expression.
        return Expression(symbol="+", left_child=p.expr0, right_child=p.expr1)

    # The substraction rule.
    @_("expr MINUS expr")
    def expr(self, p):
        # Building a new Node for this expression.
        return Expression(symbol="-", left_child=p.expr0, right_child=p.expr1)

    # The multiplication rule.
    @_("expr TIMES expr")
    def expr(self, p):
        # Building a new Node for this expression.
        return Expression(symbol="*", left_child=p.expr0, right_child=p.expr1)

    # The division rule.
    @_("expr DIVIDE expr")
    def expr(self, p):
        # Building a new Node for this expression.
        return Expression(symbol="/", left_child=p.expr0, right_child=p.expr1)

    # Handling parenthesis.
    @_("LPAREN expr RPAREN")
    def expr(self, p):
        # Forwarding the expression inside the parenthesis.
        return p.expr

    # Recognizing numbers.
    @_("NUMBER")
    def expr(self, p):
        # Building a leaf for the AST.
        return Number(p.NUMBER)

################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
