def sumCheck(a,s):
    found = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == s:
                found = found + 1
                print(a[i],a[j])
    return found

a = [6,4,7,3,8,2,1,11,20]
s = 10
print("Number of pairs found :", sumCheck(a,s))

