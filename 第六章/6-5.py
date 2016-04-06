# -*- coding:utf-8 -*-

__author__ = 'Yuriy'

'''
6–5. 字符串
(a)更新你在练习 2-7 里面的方案,使之可以每次向前向后都显示一个字符串的一个字符.
	注：2-7，从用户接受输入，然后逐字符显示该字符串
	理解：我这样做吧，输出的时候先定位字符串中间，然后从中间开始输出两边的字符
(b)通过扫描来判断两个字符串是否匹配(不能使用比较操作符或者 cmp()内建函数)。附加题：
在你的方案里加入大小写区分.
	解：长度匹配？每个字符匹配？
(c)判断一个字符串是否重现(后面跟前面的一致).附加题：在处理除了严格的回文之外,加入对
例如控制符号和空格的支持。
	解：这题题目给的有问题，前面跟后面的一致？那只需要判断前后两部分是不是重复就行。
(d)接受一个字符,在其后面加一个反向的拷贝,构成一个回文字符串.
	解:字符串的切片操作
'''

import sys
def funA():
	myStr = raw_input("input a string:\n")
	length = len(myStr)
	if length == 0:
		print 'input something!'
		sys.exit()
	i = length/2

	if length % 2 == 0:
		print 'the mid char is %s %s' %(myStr[length-1-i], myStr[i])
		#优化：myStr[i] ,myStr[-(i+1)] 以左边的为i
		i += 1
	else:
		print 'the mid char is %s ' % myStr[i]
		i += 1

	flag = False
	str = 'Type Y/N to continue to output the pre and next letter '
	print str
	while not flag:

		ch = raw_input('Y/N >>>').lower()
		if i > length - 1:
			print 'THE END! The str has Done!'
			sys.exit()
		if ch == 'y':
				print myStr[length-1-i], myStr[i]
				i += 1
		else:
			flag = True

# funA()

def funB():
	st1 = raw_input('字符串1:')
	st2 = raw_input('字符串2:')
	i = 0
	if len(st1) != len(st2):
		return False
	for i in range(len(st1)):
		if st1[i] != st2[i]:
			return False
	else:
		return True

# print funB('abc', 'abc')

def funC():
	ch = raw_input('input something')
	for c in ch:
		if ch.find(c) != ch.rfind(c):
			return False
	else:
		return True


def funD():
	li = ''
	ch = raw_input('input something\n>>>')
	li = '%s%s' %(ch, ch[::-1])
	print li


def main():
	msg = {'1': funA, '2': funB, '3': funC, '4':funD}

	ch = raw_input('''input function number:
			1.funA
			2.funB
			3.funC
			4.funD
			5.Exit
			your choice:
	''')
	if ch == '5' or ch not in '1234':
		sys.exit()
	msg[ch]()


if __name__ == '__main__':
	while True:
		main()