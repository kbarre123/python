#!/usr/bin/python

import sys
from lxml import html
import requests

def main():
	# Command line args are in sys.argv[1], sys.argv[2]...

	for i in range(1, 7):
		#https://projecteuler.net/problems;page=1
		page = requests.get('https://projecteuler.net/problems;page=%d' % i, verify=False)
		tree = html.fromstring(page.text)

		""" Schema
		<tr>
		<td class="id_column">1</td>
		<td><a href="problem=1" title="Published on Friday, 5th October 2001, 06:00 pm">Multiples of 3 and 5</a></td>
		<td><div style="text-align:center;">436669</div></td>
		"""

		names = tree.xpath('//td[2]/a/@href')
		nums = tree.xpath('//td[3]/div/text()')

		for j in range(0, len(nums)):
			print 'page: {0:d}, {1:s}, {2:s}'.format(i, names[j], nums[j])

		# Schema changes on page 6, so we have to cobble together two scrapes into one file

	for i in range(6, 12):
		#https://projecteuler.net/problems;page=1
		page = requests.get('https://projecteuler.net/problems;page=%d' % i, verify=False)
		tree = html.fromstring(page.text)

		names = tree.xpath('//td[2]/a/@href')
		nums = tree.xpath('//td[3]/div/a/text()') # The number moved into an <a> element here

		for j in range(0, len(nums)):
			print 'page: {0:d}, {1:s}, {2:s}'.format(i, names[j], nums[j])

if __name__ == '__main__':
    main()


