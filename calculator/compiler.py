#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-06
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
from typing import Tuple    # Used for type hints.


# External imports 
# Your imports from other packages go here 


# Internal imports 
from calculator.ast import Tree, Node, Number, Expression   # Used for downcasts.

################################### CLASSES ####################################

class MathCompiler:
    """
    Compiles the AST into C code.
    """

    def __init__(self):
        """
        Constructor of the compiler class.
        """
        # We need to build unique names for our intermediary values, we use a counter for this.
        self.counter = 0

    def new_name(self) -> str:
        """
        Returns a new unique name for an intermediary variable.
        """
        # We build the name from the counter.
        name = f"__{self.counter}"
        # We increment the counter for the next call.
        self.counter += 1
        # We return the expected name.
        return name

    def codegen(self, ast: Tree) -> str:
        """
        Compiles the provided source code into C source code.

        Arguments
        =========
         - ast: AST description of the computation to compile.

        Returns
        =======
        The source code for the computation, as a string.
        """
        source_code = ""
        # We first have to include stdio.h for printf.
        source_code += (
            "// Including stdio.h for printf.\n"
            "#include <stdio.h>\n"
            "\n\n"
        )
        # We open the main function.
        source_code += (
            "// Entry point for the execution.\n"
            "int main (int argc, const char **argv) {\n"
            "\n"
        )
        # Recursively building code for the mathematical computation, starting
        # from the head of the AST.
        last_result_name, whole_code = self.recursive_codegen(ast.head)
        # We add the built code to the source.
        source_code += whole_code
        # We add a small snippet to print the result of the computation.
        source_code += (
            "\n"
            "\t// Printing the result of the computation.\n"
            f"\treturn printf(\"Final Result: %f\\n\", {last_result_name});\n"
            "\n"
        )
        # Closing the main function.
        source_code += (
            "}\n"
            "// EOF\n"
        )
        # Returning the expected source code.
        return source_code

    def recursive_codegen(self, node: Node) -> Tuple[str, str]:
        """
        Recursively builds C code for the provided AST Node.

        Arguments
        =========
         - node: The AST Node for which we are building the code.

        Returns
        =======
        A tuple with two element:
         - The lvalue to use this expression later in the code.
         - The code snippet for this Node.
        """
        # Two cases appear, we have to downcast our node first.
        if isinstance(node, Number):
            # Base case. We first need a name for our variable.
            name = self.new_name()
            # We build the (indented) snippet for the creation of the variable.
            snippet = (
                f"\tconst float {name} = {node.symbol};\n"
            )
            # We return the two expected values.
            return name, snippet
        else:
            # We first need to build the right and left side of the expression.
            left_name, left_snippet = self.recursive_codegen(node.left_child)
            right_name, right_snippet = self.recursive_codegen(node.right_child)
            # We create a name for our intermediary value.
            name = self.new_name()
            # We add the line to compute our intermediary value. By chance, we
            # may directly use the symbol from the parser.
            expression_snippet = (
                f"\tconst float {name} = {left_name} {node.symbol} "
                f"{right_name};\n"
            )
            # We merge the three code snippet into one that we return.
            return name, left_snippet + right_snippet + expression_snippet


################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
