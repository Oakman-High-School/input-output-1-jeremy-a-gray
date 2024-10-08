# ******************************************************************************
#
# cs-hello-world, python hello world project
#
# Copyright 2024 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# ******************************************************************************

"""Hello things."""

# Above this comment is the file banner, with basic information about
# the program and typical copyright and license information.  The
# string inside three quotation marks documents what this file does in
# the program and is only used when generating documentation.

# This line imports the ``sys`` module and allows access to system
# utilities.
import sys

# DO NOT MAKE MODIFICATIONS ABOVE THIS LINE.
# Feel free to read, though.


# This is a function.  It will print "Hello, world!".  This is the
# simplest program you can create, although it can be done more simply
# without functions and modules.
def hello_world():
    """Print "Hello, world!".

    Print "Hello, world!".

    Returns
    -------
        ``None``.
    """
    # The information above is the documentation for this function.
    # The format used above allows software that generates
    # documentation automatically to create the documentation for this
    # function.
    print("Hello, world!")


# Copy and modify the ``hello_world`` function above so that it says
# goodbye instead of hello.
def goodbye_world():
    """Print "Goodbye, world!"."""
    print("Goodbye, world!")


# This is a function, with an optional argument ``entity`` which has a
# default value of "world".  It will print "Hello, {entity}!" where
# ``{entity}`` will be replaced with the value of the variable
# ``entity``.  When called without an argument, it will behave exactly
# as ``hello_world`` above.
#
# Change the ellipses (...) to make the program behave as specified.
#
# Giving a variable a value in a function definition sets a default
# value for the variable.  If a new value is not supplied when the
# function is called, it uses the default value.
#
# Change the ellipsis to set the default value of ``entity`` to be
# "world".  This type of variable is a string and values for strings
# must be in quotation marks, either single or double.
#
# Then, change the ellipsis in the print statement below to print
# ``entity``.
def hello(entity=...):
    """Says hello to ``entity``.

    Says hello to ``entity``.

    Parameters
    ----------
    entity : str
        The entity to which to say hello.

    Returns
    -------
        ``None``.
    """
    print("Hello, " + ... + "!")


# Copy and modify the ``hello`` function above so that it says
# "Goodbye" instead of hello.
def goodbye(entity=...):
    """Says goodbye to ``entity``."""
    pass


# DO NOT MAKE MODIFICATIONS BELOW THIS LINE.
# Feel free to read, though.


# A function named ``main`` is typically the function that runs a
# program, although it is not required to have this name.  Here,
# ``main`` just runs ``hello``.
def main():
    """Run the program."""
    hello_world()


# This construct is used so that this file may work as a program or as
# a module.  When used as a program, this will run ``main``, which
# runs ``hello``, and then exits.  When used as a module, this will be
# ignored.
if __name__ == "__main__":
    sys.exit(main())
