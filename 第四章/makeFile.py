#!/usr/bin/env python
# coding = utf-8
__author__ = 'Yuriy'

'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get filename

while True:
	fname = raw_input("Please input file name:\n")
	try:
		with open(fname,'r'):  # success ,file exists ; failed, file not exists
			print "File exists"
	except IOError: #open failed
		break

#get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quite) ."

#loop until user terminates input
while True:
	entry = raw_input('>>>')
	if entry == '.':
		break
	else:
		all.append(entry)

#write lines to file with proper line-ending

fobj = open(fname, 'w')
fobj.writelines(['%s%s' %(x, ls) for x in all])
fobj.close()
print 'Done!'