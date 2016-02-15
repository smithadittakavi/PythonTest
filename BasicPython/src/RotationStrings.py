def rotation(s1,s2):
    if len(s1) != len(s2):
        print("S1 is not a rotation of S2")
        return False 
    for x in range(len(s1)):
        if s2.startswith(s1[x:]) and s2.endswith(s1[:x]):
            print("S1 is a rotation of S2")
            return True
    return False 

print(rotation('hello','lohel'))
print(rotation('hello','helloos'))
