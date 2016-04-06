# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–10.字符串.写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.
比如,输入"Mr.Ed",应该返回"mR.eD"作为输出.
'''

def reVer(ch):
	st = ''
	for i in ch:
		if i.islower():
			st += i.upper()
		elif i.isupper():
			st += i.lower()
		else:
			st += i
	return st

if __name__ == '__main__':
	print 'Input  String , Exit with q'
	while True:
		ch = raw_input('>>>')
		if ch.lower() == 'q':
			break
		print reVer(ch)