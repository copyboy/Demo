#!/usr/bin/env python
__author__ = 'Yuriy'

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input("Enter filename: ")

print

# attempt to open file for reading

try:
	fobj = open(fname,'r')
except IOError, e:
	print " *** file open error:",e

else:
	# display contents to the screen
	for eachLine in fobj:
		print eachLine.strip()
	fobj.close()

