#!/usr/bin/python

import sys
import math

def main():
	num = 2
	target = 10001

	while target > 0:
		if is_prime(num):
			target -= 1
		
		if target > 0:
			num += 1

	print num

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
