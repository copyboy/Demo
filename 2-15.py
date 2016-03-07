__author__ = 'Yuriy'

i = 0
li = []
print 'Please input three numbers'
while i < 3:
	ch = raw_input(">>>")
	try:
		li.append(int(ch))
		i += 1
	except ValueError, e:
		print 'Please input number!'

if li[0] < li[1]:
	if li[1] < li[2]:
		print "%d < %d < %d" % (li[0], li[1], li[2])
	elif li[0] < li[2]:
		print "%d < %d < %d" % (li[0], li[2], li[1])
	elif li[0] > li[2]:
		print "%d < %d < %d" % (li[2], li[0], li[1])
	else:
		print "%d = %d < %d" % (li[0], li[2], li[1])
elif li[0] > li[1]:
	if li[0] < li[2]:
		print "%d < %d < %d" % (li[1], li[0], li[2])
	elif li[1] < li[2]:
		print "%d < %d < %d" % (li[1], li[2], li[0])
	elif li[1] > li[2]:
		print "%d < %d < %d" % (li[2], li[1], li[0])
	else:
		print "%d = %d < %d" % (li[2], li[1], li[0])
else:
	if li[0] < li[2]:
		print "%d = %d < %d" % (li[1], li[0], li[2])
	elif li[0] > li[2]:
		print "%d < %d = %d" % (li[2], li[1], li[0])
	else:
		print "%d = %d = %d" % (li[2], li[1], li[0])