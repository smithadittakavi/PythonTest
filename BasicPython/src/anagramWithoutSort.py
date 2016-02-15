def isAnagram(str1,str2):
    word1=[]
    word2=[]
    for x in range(len(str1)):
        word1.append(str1[x])
    for x in range(len(str2)):
        word2.append(str2[x])
    if(len(word1)==len(word2)):
        for letter in word1:
            if letter in word2:
                word2.remove(letter)
                
    

    if len(word2)==0:
        print("S1 and S2 are anagrams")
        return True
    else:
        print("S1 and S2 are not anagrams")
        return False
        
        
        
str1 = str(input("Enter S1 : "))
str2 = str(input("Enter S2 : "))
print(isAnagram(str1,str2))

