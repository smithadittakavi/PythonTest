def permutation(word,tail=''):
   
    if len(word) == 0: 
        print(tail)
    else:
        for i in range(len(word)):
            permutation(word[0:i] + word[i + 1:], tail + word[i])

word = input("Enter a word : ")
permutation(word)
