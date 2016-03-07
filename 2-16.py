# coding = UTF-8
__author__ = 'Yuriy'

filename = raw_input("Enter file name:\n")

fobj = open(filename ,'r')
for eachLine in fobj:
	print eachLine,
fobj.close()