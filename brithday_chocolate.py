def chocolate(s,d,m):
	if m > 1:
		a = [True for i in range(len(s)-m+1) if sum(s[i:(i+m)]) == d]
		print(a.count(True))
	else:
		if s[0] == d:
			print(1)
		else:
			print(0)

s = [1,1,1,1,1,1]
d = 3
m = 2

print(chocolate(s,d,m))
