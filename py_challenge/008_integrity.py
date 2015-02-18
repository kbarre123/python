#!/usr/bin/python

# http://www.pythonchallenge.com/pc/def/integrity.html

import sys, bz2

def main():
	un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

	# 'BZh91AY&SYA' is the flag of bzip2 compress method (and 'PK/x03/x04' is that of zip)
	# So, we know the uname/pword are compressed. And the hint on the page is 'inflate', so
	# let's uncompress them.
	print bz2.decompress(un)
	print bz2.decompress(pw)

if __name__ == '__main__':
    main()
