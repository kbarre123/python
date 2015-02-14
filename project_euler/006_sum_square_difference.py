#!/usr/bin/python

import sys

# Gather our code in a main() function
def main():
	limit = 100
	sum_squares = 0
	square_of_sums = 0
	_sum = 0
	difference = 0

	# Calculate the sum of the squares of x = {1..100}
	for x in range(1,limit + 1):
		sum_squares += pow(x, 2)

	# Calculate the square of the sum of y = {1..100}
	for y in range(1,limit + 1):
		_sum += y
	
	square_of_sums = pow(_sum, 2)

	# Calculate the difference b/t the two
	difference = square_of_sums - sum_squares
	print difference 

if __name__ == '__main__':
    main()
