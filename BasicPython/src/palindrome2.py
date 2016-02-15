def is_palindrome(s):
    l=len(s)
    list_s=list(s)
    for i in range(0,l):                                            
        if(list_s[i] !=list_s[l-i-1]):
            print ("Is NOT Palindrome")
            return False
        
        else:
            print ("Is Palindrome")
            return True
        
s = input("Enter string :")
s1 = is_palindrome(s)
