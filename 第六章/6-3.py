# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–3. 排序
(a) 输入一串数字,从大到小排列之.
(b) 跟 a 一样,不过要用字典序从大到小排列之.
理解：字典序，以字符串比较大小，而不是数字
'''

import sys

def funA():
	li = []
	ch = raw_input('请输入一行数字，以空格分隔：')
	for i in ch.split():
		li.append(int(i))

	print li
	print sorted(li, reverse=True)


def funB():
	ch = raw_input('请输入一行数字，以空格分隔：')
	li = []
	for i in ch.split(' '):
		li.append(i)

	li.sort(reverse=True)
	print li

def main():
	st = '''
please input function number:
		1. funA
		2. funB
		3. Exit

input your choice:
'''
	ch = raw_input(st)
	msg = {'1': funA, '2': funB, '3': 'Exit'}
	if ch != '1' and ch != '2':
		sys.exit()
	else:
		msg[ch]()

if __name__ == '__main__':
	while True:
		main()