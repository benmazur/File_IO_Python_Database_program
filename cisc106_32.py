"""
CISC106 Module that includes some basic helper functions
such as check_expect

Versions:
4-17-12 Modified by Paul Amer
 + removed graphics stuff; just kept AssertEqual
9-8-11 Modified by Paul Amer
 +improved success-failure messages
0.12
 + display can be called multiple times
 + assertEqual supports PIL.Image.Image
0.1
 + Initial assertEqual, display, animate, bind
"""
__version__ = 0.12

import sys, traceback, types, os
#import Tkinter
#from PIL import Image, ImageTk

success = 0
fail = 0

def assertEqual(x, y, *args):
    """
    Checks an expected value using the isEqual function.
    Prints a message if the test case passed or failed.
    """
    
    trace = traceback.extract_stack()
    frame = trace[len(trace)-2]
    global success, fail
    
    # messages modifed 9-9-11  PDA
    # variables fail and success not used
    if not isEqual(x, y, *args):
        fail += 1
        print ("[line %d] %s FAILURE, predicted answer was %s, computed answer was %s " \
            % (frame[1], frame[3], y, x))
    else:
        success += 1
        print ("[line %d] %s SUCCESS" % (frame[1], frame[3]))
    
def isEqual(x, y, *args):
    """
    isEqual : thing thing -> boolean
    isEqual : number number number -> boolean
    Determines whether the two arguments are equal, or in the case of
    floating point numbers, within a specified number of decimal points
    precision (by default, checks to with 4 decimal points for floating
    point numbers).
    
    Examples:
    >>> isEqual('ab', 'a'+'b')
     True
     
    >>> isEqual(12.34, 12.35)
     False
     
    >>> isEqual(12.3456, 12.34568, 4)
     True
         
    >>> isEqual(12.3456, 12.34568w5)
     False
    """
    if (x is None and y is not None) or (y is None and x is not None):
        return False
    elif x is None and y is None:
        return True
    elif type(x) == int and type(y) == int:
        return x == y
    elif type(x) == float or type(y) == float:
        if len(args) == 1:
            error = 10 ** (- args[0])
        else:
            error = 0.0001
        return abs(x - y) < error
    elif isseqtype(x) and isseqtype(y) and len(x)==len(y):
        res = True
        for (x1,y1) in zip(x, y):
            res = res and isEqual(x1, y1, *args)
        return res
    else:
        return x == y

def isseqtype(x):
    return type(x) == list or type(x) == tuple

def print_verbose(obj):
    for f in dir(obj):
        print (f, "=", getattr(obj, f))


