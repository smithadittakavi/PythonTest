def isprime(x):
    x = abs(int(x))
    if x < 2:
        return "Less 2", False
    elif x == 2:
        print("Is a Prime number")
        return True
    elif x % 2 == 0:
        print("Is not a prime number")
        return False    
    else:
        for n in range(3, int(x**0.5)+2, 2):
            if x % n == 0:
                return n, False
            return True
        
x = input("Enter a number : ")
y = isprime(x)
print(y)