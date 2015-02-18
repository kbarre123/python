#!/usr/bin/python

import sys
import re

def main():
	with open('004_data.txt', 'r') as f:
		text = f.read()
		ans = "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", text))

		print  ans
	f.close()

if __name__ == '__main__':
    main()
