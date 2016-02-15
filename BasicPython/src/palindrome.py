# 121 Read both ways is the same    pip = pip in both ways etc
a = input("Enter a string : ")
def palindrome(a):
    i = 0
    while i <= len(a):
        if a[i] == a[-1-i]:
            i = i+1
            return True
        return False
if palindrome(a) == True:
    print('YES PALIN')
else:
    print('NO PALIN')