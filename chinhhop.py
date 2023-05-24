n,k=map(int,input('Nhap n,k:').split())
def fact(x):
	if x==0:
		return 1
	return x*fact(x-1)
ch=fact(n)/(fact(k)*fact(n-k))
print(ch)