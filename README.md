# Calculator

This project is a small work on programming languages, and in particular on Lexer, Parsers and ASTs. The codebase implements a very simple calculator which works in 3 steps.

1. A [MathLexer](calculator/lexer.py) tokenizes the mathematical expression.
2. A [MathParser](calculator/parser.py) builds an [AST](calculator/ast) from the tokens.
3. A [MathIntepreter](calculator/interpreter.py) performs the computation described in the AST.

Optionaly, a compiler can be used to generate C code from the calculator. This C code can be used to create an executable which prints the result of the computation. The compilation process remains very similar.

1. A [MathLexer](calculator/lexer.py) tokenizes the mathematical expression.
2. A [MathParser](calculator/parser.py) builds an [AST](calculator/ast) from the tokens.
3. A [MathCompiler](calculator/compiler.py) creates the C code from the AST.

# Installation

To install the calculator in your environment, just run:

```bash
# From the folder containing the README and the setup.py
pip3 install .
```

# Usage

The calculator provides a CLI frontend. Two modes are avaiable:

```bash
# For the REPL,
calculator -
# To run the expression from a text file,
calculator $source_code
```

By default the calculator will use an interpreter to compute what is asked, but it can also be made to output a C code that will print the result of the computation. The syntax becomes:

```bash
calculator --compiler --output code.c source_computation.txt
```

### METADATA

Field | Value
--- | ---
:pencil: Contributors | roadelou
:email: Contacts | 
:date: Creation Date | 2021-03-05
:bulb: Language | Markdown Document

### EOF
