def mahoa(c,k):
	a='abcdefghijklmnopqrstuvwxyz'
	out=''
	for i in c:
		if i==' ':
			out+=' '
		else:
			index=a.index(i.lower()) + k
			if i.islower():
				out+=a[index]
			else:
				out+=a[index].upper()
	return out
def giai(c,k):
	a='abcdefghijklmnopqrstuvwxyz'
	out=''
	for i in c:
		if i==' ':
			out+=' '
		else:
			index=a.index(i.lower()) - k
			if i.islower():
				out+=a[index]
			else:
				out+=a[index].upper()
	return out
c=input('Nhap chuoi ki tu:')
k=int(input('Nhap k:'))
print(mahoa(c,k))
print(giai(mahoa(c,k),k))