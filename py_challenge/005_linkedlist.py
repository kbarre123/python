#!/usr/bin/python

from lxml import html
import requests

def main():
	results = []
	ans = []
	link = '12345'
	for i in range(1,401):
		page = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % link)
		#print 'status code:', page.status_code
		text = page.text.split()
		link = text[-1]
		results.append(link)

	print "results"
	print results
	print '\n'

	for result in results:
		if result[0].isalpha():
			ans.append(result)

	print ''.join(ans)

if __name__ == '__main__':
    main()


