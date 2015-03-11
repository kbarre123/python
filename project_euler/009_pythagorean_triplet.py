#!/usr/bin/python

import sys, math

def main():
	a, b, c = 0, 0, 0
	found = False
	for i in range(200, 300):
		if found:
			break
		a = i
		for j in range(300, 400):
			if found:
				break
			b = j
			for k in range(400, 500):
				c = k
				if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
					if (a + b + c) == 1000:
						print a, b, c
						found = True
						break
				else:
					print a, b, c

	ans = a * b * c
	print ans

if __name__ == '__main__':
    main()
