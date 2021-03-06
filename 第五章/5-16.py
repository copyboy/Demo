# coding:utf-8
__author__ = 'Yuriy'

'''
5-16 家庭财务。给定一个初始金额和月开销数， 使用循环，确定剩下的金额和当月的支
出数， 包括最后的支出数。 Payment() 函数会用到初始金额和月额度， 输出结果应该类似下
面的格式（例子中的数字仅用于演示） ：
	Enter opening balance:100.00
	Enter monthly payment: 16.13
	Amount Remaining
	Pymt# Paid Balance
	----- ------ ---------
	0 $ 0.00 $100.00
	1 $16.13 $ 83.87
	2 $16.13 $ 67.74
	3 $16.13 $ 51.61
	4 $16.13 $ 35.48
	5 $16.13 $ 19.35
	6 $16.13 $ 3.22
	7 $ 3.22 $ 0.00
'''
def payment(a, b):
	str = '''
Amount Remaining
Pymt# Paid   Balance
----- ------ ---------
'''
	print str,
	flag = True
	i = 0
	while flag:
		if i == 0:
			print '0   $ 0.00  $ %.2f' % a
			i += 1
			continue
		if a > b:
			a -= b
			print '%d   $ %.2f  $ %.2f' % (i, b, a)
			i += 1
			continue
		else:
			print '%d   $ %.2f  $ 0.00' % (i, a)
			flag = False

def show():
	try:
		ch = float(raw_input('Enter opening balance:'))
		cj = float(raw_input('Enter monthly payment:'))
	except Exception, e:
		print '请输入正确的数字'
	payment(ch, cj)

if __name__ == '__main__':
	show()