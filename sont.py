def sont(x):
	if x<=1:
		return True
	else:
		for i in range(2,int(x**0.5)+1):
			if x%i==0:
				return False
	return True
n=int(input('Nhap so:'))
if sont(n):
	print('La so nt')
else:
	print('Khong phai so nt')