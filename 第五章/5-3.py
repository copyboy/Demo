__author__ = 'Yuriy'

def checkDegree(ch):
	ch /= 10
	if ch > 10 or ch < 0:
		print 'Please input correct score!'
	elif ch < 6:
		print 'Degree F !'
	elif ch < 7:
		print 'Degree D !'
	elif ch < 8:
		print 'Degree C !'
	elif ch < 9:
		print 'Degree B !'
	else:
		print 'Degree A !'

if __name__ == '__main__':
	ch = int(raw_input("input your score:"))
	checkDegree(ch)
