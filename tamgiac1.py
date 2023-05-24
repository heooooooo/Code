#pylint:disable=W0621
import time
def quick_sort(arr):
	if len(arr)<=1:
		return arr
	pivot=arr[len(arr)//2]
	left=[x for x in arr if x<pivot]
	middle=[x for x in arr if x==pivot]
	right=[x for x in arr if x>pivot]
	return quick_sort(left)+middle+quick_sort(right)

def selection_sort(arr):
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			if arr[i]>arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
	return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
f=open('tamgiac.inp')
a=list(map(int,f.readline().strip().split()))
n=int(input('Nhap:'))
if n==1:
	print(selection_sort(a))
elif n==2:
	print(bubble_sort(a))
elif n==3:
	print(merge_sort(a))
else:
	print(quick_sort(a))
print(time.process_time())
f.close()
	