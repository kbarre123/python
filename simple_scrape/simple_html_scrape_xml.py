from lxml import html
import requests

page_num = 5

for i in range(1, (page_num + 1)):
	page = requests.get('http://econpy.pythonanywhere.com/ex/00%d.html' % i)
	tree = html.fromstring(page.text)

	""" Target XML Structure
	<div title="buyer-name">Carson Busses</div>
	<span class="item-price">$29.95</span><br>
	"""

	#This will create a list of buyers:
	buyers = tree.xpath('//div[@title="buyer-name"]/text()')
	#This will create a list of prices
	prices = tree.xpath('//span[@class="item-price"]/text()')

	for j in range(0, len(buyers)):
		#print "%d.%d" % (i, j), buyers[j], ",", prices[j]
		print '{0:02d}.{1:02d} {2:s} {3:s}'.format(i, j, buyers[j], prices[j])
