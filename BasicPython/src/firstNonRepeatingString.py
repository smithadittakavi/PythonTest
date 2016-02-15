def firstNonRep(word):
    count = {}
    for c in word:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for c in word:
        if count[c] == 1:
            return c
word = "hello"
print(firstNonRep(word))


# SECOND METHOD : 


 

 
'''
returns the first non repeated character in an input string.
there will be no difference between a capital and lowercase letter
if it was a ' ', then it will not return anything.
'''
def find_nonrepeated(string):
    table = {}
 
    # build a dictionary containing each character in the string
    # and a counter of how many appearances it shows up in the
    # string
    for char in string:
        if char in table:
            table[char] += 1
        elif char != " ":
            table[char] = 1
        else:
            table[char] = 0
 
    # loop through each character in the string once the dictionary
    # is built, and check for the number of appearances. once we find
    # a count of 1, we will return
    for char in string:
        if table[char] == 1:
            print("the first non repeated character is: %s" % (char))
            return char
 
    return
 
string = input("Enter your string: ")
find_nonrepeated(string)