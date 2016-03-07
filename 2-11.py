# coding = utf-8
__author__ = 'Yuriy'

def Add5():
	li = []
	while True:
		ch = raw_input(">>>")
		if ch == 'end':
			break
		elif ch == 'help':
			print 'Enter \'end\' to finish the input'
		elif ch.isdigit():
			li.append(ch)
		else:
			print 'Please input numbers!'
	print li
	i = 0
	values = 0
	for i in range(len(li)):
		values += int(li[i])
		i += 1
	print values
def Average5():
	li = []
	while True:
		ch = raw_input(">>>")
		if ch == 'end':
			break
		elif ch == 'help':
			print 'Enter \'end\' to finish the input'
		elif ch.isdigit():
			li.append(ch)
		else:
			print 'Please input numbers!'
	print li
	i = 0
	values = 0
	for i in range(len(li)):
		values += int(li[i])
		i += 1
	print values / float(len(li))

while True:
	print '''
	(1)Function Add
	(2)Function Div
	(X)Exit
	'''
	ch = raw_input("please select the function:")
	if ch == 'X':
		break
	elif int(ch) == 1:
		Add5()
	elif int(ch) == 2:
		Average5()
	else:
		print 'please input correct option !'


