#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        stderr.write("Exception: {}\n".format(err.args[0]))
        return False
    except ValueError as err:
        stderr.write("Exception: {}\n".format(err.args[0]))
        return False
