#!/usr/bin/python

import sys
import pickle

def main():
	banner = pickle.load(open('006_data.txt', 'r'))
	data = []
	for item in banner:
		print 'item:', item
		for seq in item:
			data.append(seq[0]*seq[1])
		data.append('\n')

	print ''.join(data)

if __name__ == '__main__':
    main()
