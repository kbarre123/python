#!/usr/bin/python

import sys, math

def main():
	# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
	a, b, c = 0, 0, 0
	found = False
	for i in range(200, 300):
		if found:
			break
		a = i
		for j in range(1, 300):
			if found:
				break
			b = j
			for k in range(1, 300):
				c = k
				if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
					if a < b and b < c:
						if a + b + c == 1000:
							print "ans = ", a, b, c
							found = True
							break
				else:
					print a, b, c

if __name__ == '__main__':
    main()
