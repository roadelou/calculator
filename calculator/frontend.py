#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-06
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
import argparse # Used for the cli interface


# External imports 
# Your imports from other packages go here 


# Internal imports 
from calculator.lexer import MathLexer  # Used for the execution
from calculator.parser import MathParser    # Used for the execution
from calculator.interpreter import MathInterpreter  # Used for the execution

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def main():
    """
    Entry-point for the calculator frontend.
    """
    # We first build the cli with argparse.
    cli_parser = build_frontend_parser()
    # Parsing the command line arguments.
    arguments = cli_parser.parse_args()
    # Two cases appear:
    # - If the source code was provided, we execute it and print the result.
    # - Else we go to the repl.
    if arguments.SOURCE == "-":
        run_repl()
    else:
        run_from_source(arguments.SOURCE)

def build_frontend_parser() -> argparse.ArgumentParser:
    """
    Returns a CLI parser for the calculator frontend built with argparse.
    """
    cli_parser = argparse.ArgumentParser(prog="calculator")
    # Specifying the source code to use. If "-", stdin should be used.
    cli_parser.add_argument(
        "SOURCE", type=str, help="The source file to execute"
    )
    # Returning the built parser.
    return cli_parser

def run_repl():
    """
    Runs the MathInterpreter in REPL mode.
    """
    # Creating the lexer, parser and interpreter used for the repl.
    lexer = MathLexer()
    parser = MathParser()
    interpreter = MathInterpreter()

    # Running the global loop.
    while True:
        # Read the user input.
        try:
            user_input = input(">> ")
        except EOFError:
            # End of the repl loop.
            break
        # Lexing the input.
        tokens = lexer.tokenize(user_input)
        # Parsing the tokens.
        ast = parser.parse(tokens)
        # Evaluating the AST.
        result = interpreter.run(ast)
        # Printing the result back to the user.
        print(result)


def run_from_source(source_code_path: str):
    """
    Runs the provided source code with the interpreter.

    Arguments
    =========
     - source_code_path: The path to the source file that should be executed.
    """
    # We start by reading the source file.
    with open(source_code_path, "r") as source_code_file:
        source_code = source_code_file.read()

    # We create a lexer, parser and interpreter.
    lexer = MathLexer()
    parser = MathParser()
    interpreter = MathInterpreter()

    # Tokenizing the source code.
    tokens = lexer.tokenize(source_code)
    # Parsing the tokens.
    ast = parser.parse(tokens)
    # Evaluating the computation described in the AST.
    result = interpreter.run(ast)
    
    # We simply print the result back to the user.
    print(result)

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
