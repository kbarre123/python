#!/usr/bin/python

# Recursion
def countdown(n):
    if n <= 0:
        print "Blastoff!!!"
    else:
        print n
        countdown(n - 1)

countdown(3)

''' 
3
2
1
Blastoff!!!
'''
print

# Recursion
def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)

print_n(2, 2)

"""
2
2
"""