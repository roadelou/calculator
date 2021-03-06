#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-05
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
from setuptools import setup    # Used to build the python package.


# External imports 
# Your imports from other packages go here 


# Internal imports 
# Your imports within this package go here 

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def main():
    """
    Calls the setup function to define the python package.
    """
    setup(
        name="calculator",
        version="0.0.2",
        author="roadelou",
        author_email="",
        packages=[
            "calculator",
            "calculator/ast"
        ],
        license="GPL3",
        install_requires=["sly"],
        python_requires=">=3.6",
        entry_points="""
        [console_scripts]
        calculator=calculator.frontend:main
        """
    )

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    main()

##################################### EOF ######################################
