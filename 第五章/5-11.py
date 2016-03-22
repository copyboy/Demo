# coding:utf-8
__author__ = 'Yuriy'

'''
5-11 取余。
(a) 使用循环和算术运算，求出 0－20 之间的所有偶数
(b) 同上，不过这次输出所有的奇数
(c) 综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么？
(d) 使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 先要求用户输
入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回 True 和 False;
'''

def funcA():
	li = [x for x in range(21) if x % 2 == 0]
	print li

def funcB():
	li = [x for x in range(21) if x % 2 ]
	print li

def funcC():
	print '对2取余操作是最简单的判别奇数偶数的方法'

def funcD():
	try:
		a = int(raw_input('输入整数a:'))
		b = int(raw_input('输入整数b:'))
	except Exception:
		print '请输入整数！'
	if b > a:
		a, b = b, a
	x = a % b
	if x == 0:
		print 'True'
		return True
	else:
		print 'False'
		return False
def err():
	print 'something error.'
def show():
	while True:
		str = '''
	func 1:20中的偶数
	func 2:20中的奇数
	func 3:奇数偶数的判断方式
	func 4:判断两个数是否有整除关系
'''
		print str
		ch = raw_input('input function number:')

		msg = {'1': 'funcA()', '2': 'funcB()', '3': 'funcC()', '4': 'funcD()'}
		if ch not in msg.keys():
			print '请输入正确的功能序号！'
			continue
		eval(msg.get(ch))

if __name__ == '__main__':
	show()