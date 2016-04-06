# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–6. 字符串.创建一个 string.strip()的替代函数:接受一个字符串,去掉它前面和后面的
空格(如果使用 string.*strip()函数那本练习就没有意义了)
	解：先去除前面的空格，然后从前面非空格处遍历，直到为空格停止
'''

def myStrip(str):
	i = 0
	length = len(str)
	li = [i for i in range(length) if str[i] != ' ']
	print li
	st = ''
	j = li[0]
	while str[j] != ' ':
		st += str[j]
		j += 1
	return st

print len(myStrip('   3gekongge  '))

