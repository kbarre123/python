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
	treasure = []

	def check_clue(clue):
		"""
		Read current clue. If cell value is same as clue, stop. Else, update
		current clue. 
		"""
		global current_clue
		new_clue = str(treasure_map[clue[0]-1][clue[1]-1])
		current_clue = [int(new_clue[0]), int(new_clue[1])]
		print "During: [%d, %d]" % tuple(current_clue)
		return current_clue
	 
	print "Before: [%d, %d]" % tuple(current_clue)
	check_clue(current_clue)
	print "After:  [%d, %d]" % tuple(current_clue)

if __name__ == '__main__':
    main() 
