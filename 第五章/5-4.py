__author__ = 'Yuriy'

def decideLeap(ch):
	if ch % 4 == 0 and ch % 100 != 0 or ch % 400 == 0:
		print '%d is Leap Year' % ch
	else:
		print '%d is not a Leap Year ' % ch


if __name__ == '__main__':
	ch = int(raw_input("Please input of the year:"))
	decideLeap(ch)