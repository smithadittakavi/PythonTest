#count = 0
#ind = 0
#name = input("Enter your name: ")
#for vowel in name:
#    for cons in name:
#        if vowel in ['a','e','i','o','u']:
#            count = count + 1
#        elif cons not in ['a','e','i','o','u']:
#            ind = ind+1
#print("You have",ind,"vowels")

count = 0
ind = 0
name = input("Enter your name: ")
for cons in name:
    if cons not in ['a','e','i','o','u']:
            count = count + 1
            print("Consonants are :",cons)
print("You have",count,"consonants")
for vowels in name:
    if vowels in ['a','e','i','o','u']:
        ind = ind+1
        print("Vowels are :",vowels)
print("You have",ind,"vowels")




        

    