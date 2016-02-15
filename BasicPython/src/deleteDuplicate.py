#Delete duplicates in a string
print("Enter the String:")
foo = input()

result = []
for i in foo:
    if i not in result:
        result.append(i)
result = ''.join(result)
print(result)


#Delete duplicates in a list 

print("Enter list :")
lst = input()

r = []
for i in lst:
    if i not in r:
        r.append(i)
r = ''.join(r)
print(r)



