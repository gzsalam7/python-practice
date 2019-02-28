#lab 7 practice assignment 
class listSearch:
    def __init__(self):
        self.l = []

    def addList(self,x):
        self.l = self.l + [x]

    def returnList(self):
        return self.l

    def searchList(self,x):
        for i in range(len(self.l)):
            if self.l[i] == x:
                return i
        return -1

    def deleteListEnd(self):
        self.l = self.l[:-1]
            

    
        
myObject = listSearch()
