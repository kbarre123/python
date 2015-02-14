#!/usr/bin/python

import math

def main():
	array = []

	for i in range(999, 0, -1): # change back to 999
	    for j in range(999, 0, -1): # change back to 999
	        product = i * j
	        if is_palindrome(product):
	            array.append(product)
	           
	print max(array) 
	print array

def is_palindrome(p):
	if str(p) == str(p)[::-1]:
	    return True

if __name__ == '__main__':
    main()
