#!/usr/bin/python

import sys

def main():
	for i in range(0, len(ints)):
    	for j in range(0, len(ints)):
            if ints[i] + ints[j] == s:
                return ints[i], ints[j]

if __name__ == '__main__':
    main()
