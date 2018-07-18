'''
s = str(input('请输入一个整形数'))

i = 0
j = -1
while s[i] <= len(s/2):
	if s[i] = s[j]
		i +=1
		j -=1
	else:
		break
print('{}是一个整形数'.format(s))
'''
m = 0
for num in range(100,1001):
	i = 2
	if i < num:
		if num % i == 0:
			num = num + 1
			break
		elif num % i != 0:
			i = i +1
		m = m + 1
print('{}'.format(m))












