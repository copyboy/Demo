# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–12.字符串
(a)创建一个名字为 findchr()的函数,函数声明如下:
def findchr(string, char)
findchr()要在字符串 string 中查找字符 char,找到就返回该值的索引,否则返回-1.不能用
string.*find()或者 string.*index()函数和方法
(b)创建另一个叫 rfindchr()的函数,查找字符 char 最后一次出现的位置.它跟 findchr()工作
类似,不过它是从字符串的最后开始向前查找的.
(c)创建第三个函数,名字叫 subchr(),声明如下:
def subchr(string, origchar, newchar)
subchr()跟 findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符.返回
修改后的字符串.
'''
def findchr(string, char):
	for i in range(len(string)):
		if string[i] == char:
			return i
	else:
		return -1

def rfindchr(string, char):
	print string
	for i in range(len(string)):
		if string[-i-1] == char:
			return len(string) - (i + 1)
	else:
		return -1


def subchr(string, origchar, newchar):
	for i in range(len(string)):
		if string[i] == origchar:
			string = string[:i] + newchar + string[i+1:]
	else:
		return string


def main():
	# print rfindchr('adcc', 'c')
	# print subchr('advvc', 'v', 'z')

	print '''
	input function Number:
			1.findchr
			2.rfindchr
			3.subchr
			4.Exit
	your Choice:
'''
	while True:
		ch = raw_input('>>>')
		if ch not in '123':
			break
		elif ch == '1':
			string = raw_input('input string:')
			char = raw_input('input char:')
			print findchr(string, char)
		elif ch == '2':
			string = raw_input('input string:')
			char = raw_input('input char:')
			print rfindchr(string, char)
		else:
			string = raw_input('input string:')
			origchar = raw_input('input char:')
			newchar = raw_input('input char:')
			print subchr(string, origchar, newchar)

if __name__ == '__main__':
	main()