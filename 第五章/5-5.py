# coding:utf-8
__author__ = 'Yuriy'

def divide(x):
	y = x * 100
	a = y // 25
	b = (y - a * 25) // 10
	c = (y - a * 25 - b * 10) // 5
	d = y - a * 25 - b * 10 - c * 5
	chx = {}
	if a != 0:
		chx[25] = a
	if b != 0:
		chx[10] = b
	if c != 0:
		chx[5] = c
	if d != 0:
		chx[1] = d
	# print ch
	# print chx
	print '%.2f美元换算结果:' % x
	for i in range(len(chx)):
		print '%d个%d美分'%( chx.values()[i],chx.keys()[i]),
	print
if __name__ == '__main__':
	while True:
		try:
			ch = float(raw_input("\nInput the number of dollars|$|:"))
		except ValueError,e:
			print 'Please input the correct number !'
			continue
		divide(ch)
