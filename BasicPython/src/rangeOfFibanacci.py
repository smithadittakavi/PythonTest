lower = int(input("Enter lower :"))
upper = int(input("Enter Upper :"))
a = 0
b = 1
for num in range(lower,upper+1):
    temp = a
    a = b
    b = temp + b  
    print(a)
    

