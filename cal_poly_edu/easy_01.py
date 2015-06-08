#!/usr/bin/python

import sys

def main():

	treasure_map = [
		[34, 21, 32, 41, 25],
		[14, 42, 43, 14, 31],
		[54, 45, 52, 42, 23],
		[33, 15, 51, 31, 35],
		[21, 52, 33, 13, 23]
	]

	current_clue = [1,1]
	print current_clue

	def check_clue(clue):
		new_clue = str(treasure_map[current_clue[0]-1][current_clue[1]-1])
		row = new_clue[0]
		col = new_clue[1]
		current_clue[0] = int(row)
		current_clue[1] = int(col)
		print current_clue

	check_clue(current_clue)

if __name__ == '__main__':
    main()
