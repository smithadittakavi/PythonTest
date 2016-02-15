def ascOrder(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            return alist

alist = [15, 12, 10]
b = ascOrder(alist)
print(b) # --> b = [10, 12, 15]
c = 13
for i in range(len(b)):
    if b[i] > c:
        index = i
        break
d = b[:i] + [c] + b[i:]
print(d) # --> d = [10, 12, 13, 15]

