# coding:utf-8
__author__ = 'Yuriy'

'''
5–15. 最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。
辗转相除法：
例：24 18
24 / 18 = 1  ... 6
18 / 6  = 3  ... 0 当余数为0时，此时的除数就是最大公约数
'''

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, divmod(a, b)[1])

def g(a, b):
	if a > b:
		return b * gcd(a, b)
	else:
		return a * gcd(a, b)

def show():
	while True:
		try:
			a = int(raw_input('\n输入正整数a\n>>>'))
			b = int(raw_input('输入正整数b\n>>>'))
		except Exception:
			print '输入错误，请重新输入'
			continue
		print '最大公约数：%d' % gcd(a, b)
		print '最小公倍数：%d' % g(a, b)


if __name__ == '__main__':
	show()