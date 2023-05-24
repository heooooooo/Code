m,n=map(int,input('m,n=').split())
tich=m*n
while m!=n:
	if m>n:
		m-=n
	else:
		n-=m
bcnn=tich/m
print('UCLN=',m)
print('BCNN=',bcnn)