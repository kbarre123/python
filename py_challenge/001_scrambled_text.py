#!/usr/bin/python

from string import maketrans

def main():
	out_alpha = 'abcdefghijklmnopqrstuvwxyz'
	in_alpha = 'yzabcdefghijklmnopqrstuvwx'
	switch = maketrans(in_alpha, out_alpha)

	message = "map"

	print  message.translate(switch)

if __name__ == '__main__':
    main()
