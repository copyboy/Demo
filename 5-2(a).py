__author__ = 'Yuriy'

def multi(a, b):
	return a * b

if __name__ == '__main__':
	x = int(raw_input("input number:"))
	y = int(raw_input("input number:"))
	print '%d * %d = %d' % (x, y, multi(x, y))