#!/usr/bin/python

# http://www.pythonchallenge.com/pc/def/integrity.html
import urllib, zipfile, re

def main():
	file_path = '/home/kcb/Documents/code/python/py_challenge/007_zip_file.zip'
	my_file = urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', file_path)
	print 'file downloaded to', my_file[0], '\n'

	myzip = zipfile.ZipFile(file_path, 'r')
	my_dict = dict((f.filename, (myzip.open(f.filename).read(), f.comment)) for f in myzip.filelist)
	#print my_dict

	bigstring = []
 
	def get_num(start_num):
	    key = "%s.txt" % start_num
	    next_num = re.search(r'Next nothing is (\d+)', my_dict[key][0]).group(1)
	    bigstring.append(my_dict[key][1])
	    return next_num

	output = []
	output.append('90052')
	for a in range(911):
		try:
			new_value = get_num(output[a])
			output.append(new_value)
		except:
			break

	print ''.join(bigstring)
	
if __name__ == '__main__':
    main()
