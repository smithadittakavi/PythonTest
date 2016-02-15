
#>>> s1 = 'vivid'
#>>> s2 = 'dvivi'
#>>> s3 = 'vivid'
#>>> def is_anagram(s1, s2):
#...     if s1.lower() == s2.lower():
#...         return False
#...     return sorted(s1.lower()) == sorted(s2.lower())


s1 = input("Enter the first string:")
s2 = input("Enter the second string:")

def anagramCheck(s1,s2):
    if s1.lower() == s2.lower():
        return False
    return sorted(s1.lower()) == sorted(s2.lower())
print("Anagram :", anagramCheck(s1, s2))

    