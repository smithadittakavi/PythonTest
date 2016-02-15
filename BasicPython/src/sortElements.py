#Srting in Ascending Order
def ascOrder(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
ascOrder(alist)
print(alist)

#Sorting in descending Order 
def dscOrder(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                temp = a[j+1]
                a[j+1]=a[j]
                a[j]=temp 
a = [1,5,8,9,14]
dscOrder(a)
print(a)