#!/usr/bin/env python

from is_prime import is_prime

ans = 2

for i in range(3, 10, 2):
	print "i: %d" % i
	if is_prime(i):
		ans += i

print ans