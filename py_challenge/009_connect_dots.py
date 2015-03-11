#!/usr/bin/python

import sys, os
from PIL import Image

def main():

	img = Image.new('RGB',(640,480), 'black')
	dots_1 = open('009_notes_1.txt','r').read().replace('\n','').split(',')
	pixels_1 = [(int(dots_1[i]),int(dots_1[i+1])) for i in range(0,len(dots_1),2)]
	dots_2 = open('009_notes_2.txt','r').read().replace('\n','').split(',')
	pixels_2 = [(int(dots_2[i]),int(dots_2[i+1])) for i in range(0,len(dots_2),2)]

	for pixel in pixels_1:
	    img.putpixel(pixel,255)

	for pixel in pixels_2:
	    img.putpixel(pixel,255)

	img.show()
	img.save('009_connected_dots.png')

if __name__ == '__main__':
    main()
