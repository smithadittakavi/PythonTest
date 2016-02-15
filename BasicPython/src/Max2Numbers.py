
def find2max(numbers):
    max1 = 0
    max2 = 0
    
    for number in numbers: 
        if number >= max1:
            max2 = max1
            max1 = number
        elif number >= max2:
            max2 = number
    print("Max1 is :",max1)
    print("Max2 is :",max2)            
            
numbers = [2,4,7,1,10]
find2max(numbers)
