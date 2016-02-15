
class replaceString:
    def __init__(self,old):
        self.old = old 
    
    def replace(self,oldStr,new):
        for i in range(len(self.old)):
            if oldStr == self.old[i:i+len(oldStr)]:
                self.old = self.old[:i]+new+self.old[i+len(oldStr):]
    
    def __str__(self):
        return str(self.old)
    

test_str = replaceString("hello world")
print("Before Replacing : ",test_str)
test_str.replace(" ", "%20")
print("After replacing : ",test_str)