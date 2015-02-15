#!/usr/bin/python

from is_prime import is_prime

def main():
	num = 2
	target = 10001

	while target > 0:
		if is_prime(num):
			target -= 1
		
		if target > 0:
			num += 1

	print num

if __name__ == '__main__':
    main()
