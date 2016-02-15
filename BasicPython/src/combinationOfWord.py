def combinationG(word):
    level=['']
    for v in word:
        nList=[]
        for item in level:
            new = item + v
            yield new
            nList.append(new)
        level+=nList

word =input("Enter a word : ")
print(list(combinationG(word)))