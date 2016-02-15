import itertools
def permutation(word):
    for i in range(len(word)+1):
        perms = list(itertools.permutations(word,i))
        #perms = list(itertools.combinations(word,i))
        for i in perms:
            a = ''.join(i)
            print(a)
            
word = input("Enter a word : ")
b = permutation(word)
#print(b)