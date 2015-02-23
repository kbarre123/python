#!/usr/bin/python

# a = [1, 11, 21, 1211, 111221, 
# len(a[30]) = ?

import sys

def main():
	with open('010_data.txt', 'r') as f:
		coords = f.read().replace('\n','').split(',')
		pixels = [(int(coords[i]), int(coords[i+1])) for i in range(0,len(coords),2)]

		print len(coords)
		print len(pixels)

if __name__ == '__main__':
    main()
