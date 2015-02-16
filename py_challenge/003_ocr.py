#!/usr/bin/python

import sys
from collections import Counter

def main():
	with open('003_data.txt', 'r') as f:
		text = f.read()
		frequency = Counter(text)
		print frequency

	f.close()

if __name__ == '__main__':
    main()
