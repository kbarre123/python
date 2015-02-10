#!/usr/bin/python

# Call func that prints string as right-justified (ends on column 70)
def right_justify(s):
    length = len(s)
    spaces = 70 - length
    print (" " * spaces) + s

right_justify("allen")

#                                                                 allen

# Call a func that takes a func and its parameter as parameters
def do_twice(f, g):
    f(g)
    f(g)

def print_twice(h):
    print str(h)

do_twice(print_twice, "spam")

# spam
# spam
