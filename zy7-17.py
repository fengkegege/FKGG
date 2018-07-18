'''
作业一：
import random
s = random.randint(0,9)

i = 0
while i < 3:
	sum = eval(input('请输入一0~10的随机数:'))
	if sum == s:
		print('厉害了，500万属于你')
		break
	elif sum > s: 
		print('大了，再给你一次机会')
		i += 1
		continue
	elif sum < s:
		print('大胆一点')
		i += 1
		continue



作业二：
import random
num = random.randint(0,9)
cnt = 1
while True:
	try:
		input_num = int(input('请猜测(10以内整型):'))
	except Exception:
		print('输入有误！请重新输入')
		continue
	if input_num == num:
		print('厉害了！{}次就猜对了！'.format(cnt+1))
		break
	else:
		cnt += 1
		if cnt > 3:
			print('你的三次机会耗尽了！很遗憾')
			break
		if input_num > num:
			print('大了！再来一次，你还有{}次机会'.format(3-cnt))
		else:
			print('大胆一些，太小了，你还有{}次机会'.format(3-cnt))


作业三：
cnt = 0
for r in range(4):
	for b in range(4):
		for y in range(5):
			if r + b + y == 8:
				cnt += 1
				print('红球:{},篮球:{},黄球:{}'.format(r,b,y))
print('共{}种情况'.format(cnt))
'''























