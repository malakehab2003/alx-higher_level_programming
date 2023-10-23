#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as F:
        print("Exception: {}".format(F), file=sys.stderr)
        result = None
    finally:
        return result
