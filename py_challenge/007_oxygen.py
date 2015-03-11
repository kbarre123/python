#!/usr/bin/python

import sys, re
from PIL import Image

def main():
	img = Image.open('008_oxygen.png')

	# First find the grey area. For grey, r = g = b
	# Start at the top of img and go row-by-row down until you find a pixel
	# that's grey. 
	y = 0
	while True:
	    r, g, b, a = img.getpixel((0, y)) #x is 0 since grey band starts at left side of img
	    if r == g == b:
	        break
	    y += 1

	# Each gray area is 7 pixels wide, inferred by the fact that this is exercise #7.
	# Get each grey value and skip ahead 7 px, repeat. The method 'chr' takes a value b/t
	# 0-255 and returns an ASCII value. This message yields another code that has to be further
	# 'chr'd to get the final message 'integrity'.
	message = ''.join([chr(img.getpixel((x, y))[0]) for x in range(0, img.size[0], 7)])

	out = re.findall('\d+', message)
	print out
	print ''.join(chr(int(i)) for i in out)

if __name__ == '__main__':
    main()
