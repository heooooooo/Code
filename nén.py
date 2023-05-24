s=input('Nhap day:')
s+=' '
dem=1
for i in range(1,len(s)):
	if s[i]==s[i-1]:
		dem+=1
	else:
		if dem ==1:
			print(s[i-1],end='')
		else:
			print(str(dem)+s[i-1],end='')
			dem=1