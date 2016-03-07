__author__ = 'Yuriy'

while True:
	ch = raw_input(">>>")
	if not ch.isdigit():
		print 'Please input a number!'
	elif 1 < int(ch) < 100:
		print 'Success .You have input the number :%d' % int(ch)
		break
	else:
		print 'the number must between 1~100'




