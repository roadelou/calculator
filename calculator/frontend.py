#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-06
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
from typing import Optional # Used for type hints
import argparse # Used for the cli interface
import sys  # Used for stdout


# External imports 
# Your imports from other packages go here 


# Internal imports 
from calculator.lexer import MathLexer  # Used for the execution
from calculator.parser import MathParser    # Used for the execution
from calculator.interpreter import MathInterpreter  # Used for the execution
from calculator.compiler import MathCompiler  # Used for the execution

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
    if arguments.source == "-":
        run_repl(output = arguments.output, compiler_mode=arguments.compiler)
    else:
        run_from_source(arguments.source, output = arguments.output, compiler_mode=arguments.compiler)

def build_frontend_parser() -> argparse.ArgumentParser:
    """
    Returns a CLI parser for the calculator frontend built with argparse.
    """
    cli_parser = argparse.ArgumentParser(prog="calculator")
    # Specifying the source code to use. If "-", stdin should be used.
    cli_parser.add_argument(
        "source", type=str, help="The source file to execute or compile"
    )
    cli_parser.add_argument(
        "-o", "--output", type=str, default=None, help="The file to write the output to. Default is stdout."
    )
    cli_parser.add_argument(
        "--compiler", action="store_true", help="Whether the compiler should be used. Default is interpreter."
    )
    # Returning the built parser.
    return cli_parser

def run_repl(output: Optional[str], compiler_mode: bool):
    """
    Runs the MathInterpreter in REPL mode.

    Arguments
    =========
     - output: The file to write the output to. Of None is given, then stdout
        will be used.
     - compiler_mode: Whether the compiler should be used.
    """
    # Creating the objects used for the repl.
    lexer = MathLexer()
    parser = MathParser()
    if compiler_mode:
        compiler = MathCompiler()
    else:
        interpreter = MathInterpreter()

    # Opening the output file, if required.
    if output is not None:
        output_file = open(output, "w")
    else:
        # When None is given as an output file to print, it uses stdout.
        output_file = None

    # Running the global loop.
    while True:
        # Read the user input.
        try:
            user_input = input(">> ")
        except EOFError:
            # End of the repl loop.
            # Need one more newline for the style.
            print("\n")
            break
        # Lexing the input.
        tokens = lexer.tokenize(user_input)
        # Parsing the tokens.
        ast = parser.parse(tokens)
        # Evaluating the AST.
        if compiler_mode:
            result = compiler.codegen(ast)
        else:
            result = interpreter.run(ast)
        # Printing the result back to the user.
        print(result, file=output_file)

    # Closing the output file, if necessary.
    if output is not None:
        output_file.close()



def run_from_source(source_code_path: str, output: Optional[str], compiler_mode: bool):
    """
    Runs the provided source code with the interpreter or the compiler.

    Arguments
    =========
     - source_code_path: The path to the source file that should be executed.
     - output: The file to write the output to. Of None is given, then stdout
        will be used.
     - compiler_mode: Whether the compiler should be used.
    """
    # We start by reading the source file.
    with open(source_code_path, "r") as source_code_file:
        source_code = source_code_file.read()

    # We create a lexer, parser and interpreter.
    lexer = MathLexer()
    parser = MathParser()
    if compiler_mode:
        compiler = MathCompiler()
    else:
        interpreter = MathInterpreter()

    # Tokenizing the source code.
    tokens = lexer.tokenize(source_code)
    # Parsing the tokens.
    ast = parser.parse(tokens)
    # Evaluating the computation described in the AST.
    if compiler_mode:
        result = compiler.codegen(ast)
    else:
        result = interpreter.run(ast)
    
    # We print the result to the desired location.
    if output is None:
        print(result)
    else:
        with open(output, "w") as output_file:
            output_file.write(result)

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
