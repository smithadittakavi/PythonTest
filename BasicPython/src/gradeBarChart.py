def replace(name):
    newName = ''
    for i in name:
        newChar = ''
        for char in i:
            if char == ' ':
                newChar = newChar+'%20'
            else:
                newChar = newChar+char
        newName = newName + newChar
    return newName

name = input("Enter a name : ")
g = replace(name)
print("New name after replacement is : ", g)
