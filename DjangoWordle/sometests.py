class A:
	a = 5
	l = [0 for x in range(5)]
	#l2 = [[0 for x in range(a)] for y in range(3)]
	l2p = [0 for x in range(3)]
	#l2p = 3
	l2 = []
	for x in range(a):
		l2.append(l2p)
	#l2 = [[0 for x in range(5)] for y in range(3)]

print('sometests.py')
a = A()
print(a.l2)

b = 'bcdef'
for x in b:
	print(x)

c = None

if c == None:
	print("jestem none: ", b)