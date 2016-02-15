def bubbleSort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
a = [3,8,9,2,4]
bubbleSort(a)
print(a)
