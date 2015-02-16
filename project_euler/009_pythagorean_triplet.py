#!/usr/bin/python

import sys
import math

def main():
	# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
	m = 1
	n = 1
	a = math.pow(m, 2) - math.pow(n, 2)
	b = 2 * m * n
	c = math.pow(m, 2) + math.pow(n, 2)

	print 'm:%d, n:%d, a:%d, b:%d, c:%d' % (m, n, a, b, c)

	for x in range(1,10):
		m = m + x
		for y in range(1,10):
			n = y + x
			print 'm:%d, n:%d, a:%d, b:%d, c:%d' % (m, n, a, b, c)

if __name__ == '__main__':
    main()
