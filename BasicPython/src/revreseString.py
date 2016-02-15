def rev(a):
    newa = ''
    i = len(a)-1
    while i >=0:
        newa = newa+a[i]
        i=i-1
    print(newa)
    return newa

a = str(input("Enter Text :"))
rev(a)
#a = rev(b)
#print(a)