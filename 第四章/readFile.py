#!/usr/bin/env python
__author__ = 'Yuriy'

import os
'readTextFile.py -- read and display text file'



while True:

	# get filename
	fname = raw_input("Enter filename: ")
	print
	# attempt to open file for reading
	if not os.path.exists(fname):
		print " *** file open error!\n"
	else:
		fobj = open(fname,'r')
		# display contents to the screen
		for eachLine in fobj:
			print eachLine,
		fobj.close()
		break
