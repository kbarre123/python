#!/usr/bin/python

import sys
from lxml import html
import requests

def main():
	page = requests.get('graph.facebook.com/me/friends') # need access token in this GET request
	print 'status code:', page.status_code
	print 'page_header:', page.headers

	# The request will be in JSON

if __name__ == '__main__':
    main()


