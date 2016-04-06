
words = ['awesome', 'great', 'fantastic']

list1 = []

for word in words:
	print id(word)
	list1.append(lambda: word)
	print list1[-1]()
	print 'id------------', id(list1[-1]())
# for i in range(len(words)):
# 	print id(words[i])
# 	list1.append(lambda: words[i])
# 	print list1[-1]()

print '\n', len(list1), id(list1[0]()), id(list1[1]()), id(list1[2]()), '\n'

for i in range(len(list1)):
	print i, '------', list1[i]()
	print id(list1[i]())