# Error & Exception handling
import sys

class InputError(Exception):
    """Base class for exceptions in this module."""
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message

try:
    f = open('example1.log')
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
except Exception as e:
    print("Unexpected error:", e)
    raise InputError(e)
else:
    f.close()