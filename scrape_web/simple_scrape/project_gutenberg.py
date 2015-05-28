#!/usr/bin/python

import sys
import random
from lxml import html
import requests

def main():
	# Command line args are in sys.argv[1], sys.argv[2]...

	letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	myLetter = random.choice(letterList)
	page = requests.get('https://www.gutenberg.org/browse/titles/%s' % myLetter, verify=False )
	print page
	tree = html.fromstring(page.text)

	"""Target XML Structure
	???
	"""

	book = tree.xpath('//div[@class="pgdbbytitle"]/h2/a/text()')
	print book

	# From Titles, randomly select a letter from the alphabet and go to that page
	
	# Fromm that Letter, randomly select an Title if it's in English
	# From that Title, randomly select a line from the body
	# Print the line to STDOUT 

# Standard boilerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()


