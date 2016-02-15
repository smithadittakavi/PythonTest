a = int(input("Enter length of A: "))
b = int(input("Enter length of B: "))
c = int(input("Enter length of C: "))
#To check if triangle is valid or not
if a<b+c and b<a+c and c<a+b:
    print("Valid triangle")
else:
    print("Not a triangle")
    


