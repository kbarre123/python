#!/usr/bin/python

import sys, os, re
from PIL import Image as im
from PIL import ImageDraw

def main():
	with open('009_notes_1.txt', 'r') as f:
		dots_1 = f.read().replace('\n', '').split(',')
		pixels_1 = [(int(dots_1[1]), int(dots_1[i+1])) for i in range(0, len(dots_1), 2)]
		print pixels_1

	with open('009_notes_2.txt', 'r') as f:
		dots_2 = f.read().replace('\n', '').split(',')
		pixels_2 = [(int(dots_2[1]), int(dots_2[i+1])) for i in range(0, len(dots_2), 2)]
		print pixels_2

	# Create blank img
	img = im.new('RGB', (640, 480), 'white')
	draw = ImageDraw.Draw(img)
	
	for pixel in range(0, len(dots_1), 2):
		draw.point(dots_1[pixel:pixel + 4], fill='black')

	for pixel in range(0, len(dots_2), 2):
		draw.point(dots_2[pixel:pixel + 4], fill='black')
	
	# Show img
	img.show()

if __name__ == '__main__':
    main()
