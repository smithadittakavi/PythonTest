def reverseWordOrderOfSentence(sentence):
    #break the sentence into words with split()
    words = sentence.split(' ')
    #reverse the word
    words.reverse()
    #iterate through and build the new sentence
    newSentence = ""
    for word in words:
        newSentence += " " + word
    #return and strip out beginning or trailing white space
    return newSentence.strip()

print("Enter the sentence")
sentense = str(input())
print(reverseWordOrderOfSentence(sentense))


## SECOND METHOD WITHOUT USING INBUILD reverse()
def rev(s1):
    newa = ''
    i = len(s1)-1
    while i >=0:
        newa = newa+ '' +s1[i]
        i=i-1
    return newa

s = str(input("Enter a sentence :"))
s1 = s.split()
s2 = rev(s1)
print(s2)



            
        