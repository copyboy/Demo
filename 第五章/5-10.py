# coding:utf-8
__author__ = 'Yuriy'

'''
5-10 转换。写一对函数来进行华氏度到摄氏度的转换。转换公式为 C = (F - 32) * (5 / 9)
应该在这个练习中使用真正的除法， 否则你会得到不正确的结果。
讨论：我这里使用的是正常的除法，也就是真正的除法？
'''

def ctof():
	try:
		ch = float(raw_input('华氏温度：'))
	except Exception:
		print('input error')

	c = ch * 9 / 5 + 32
	print '摄氏温度为 %.2f' % c
	return c


def ftoc():
	try:
		ch = float(raw_input('摄氏温度：'))
	except Exception:
		print('input error')
	c = (ch - 32) * 5 / 9
	print '华氏温度为 %.2f' % c
	return c

def err():
	print 'something error,input again!'

def show():
	while True:
		str = '''
func 1: 华氏转换摄氏
func 2: 摄氏转换华氏
func 3: Exit()
'''
		print str
		ch = raw_input('input function number:')
		msg = {'1': 'ftoc()', '2': 'ctof()' }
		if ch == '3':
			break
		try:
			eval(msg.get(ch))
		except Exception:
			err()

if __name__ == '__main__':
	show()