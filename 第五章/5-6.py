# coding : utf-8
__author__ = 'Yuriy'

import sys
def opr(a, b, c):
	if b == '+':
		return a + c
	elif b == '-':
		return a - c
	if b == '*':
		return a * c
	elif b == '/':
		return a / c
	if b == '%':
		return a % c
	elif b == '**':
		return a ** c
def calc(st):
	fun = ('+', '-', '*', '/', '%', '**')
	li = st.split()
	length = len(st.split())
	if length != 3:
		print 'Please input correct type!'
		return
	if li[1] not in fun:
		print 'Please input correct operator!'
		return
	if li[0].isdigit() and li[2].isdigit():   # Don't place it behind the next if status
		a = int(li[0])
		b = int(li[2])
		return opr(a, li[1], b)
	try:
		if type(float(li[0])) == type(.1) or type(float(li[2])) == type(.1):
			a = float(li[0])
			b = float(li[2])
			return opr(a, li[1], b)
	except ValueError, e:
		print 'Please input number!'
		return
	except TypeError,e:
		print 'Please input number!'
		return

def valueShow():
	while True:
		ch = raw_input('\ninput type: 1 + 2 \n>>>')
		result = calc(ch)
		if result == None:
			print 'Input again!'
		if type(result) == type(1):
			print '%s = %d' % (ch, result)
		if type(result) == type(.1):
			print '%s = %.4f' % (ch, result)
		else:
			print 'Something Error'
if __name__ == '__main__':
	valueShow()
	# x = '1 + 2'
	# y = '1+ 2'
	# z = '1 +2'
	# h = '1+2'
	# xx = 'a+b'
	# yy = '4.0 + 2.3'
	# zz = '4.a + 2.3'
	# hh = '4 d 4'
	# aa = 'a + d'

