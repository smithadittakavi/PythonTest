def removeDuplicates(string):
    result=[]
    seen=set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

string = input("Enter string : ")
b = removeDuplicates(string)
print(b)