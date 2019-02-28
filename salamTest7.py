
def main():
    CompareCombinations()
    print(PascalTriangle(6))
          
def IterativeFactorial(n):
    factorial = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(1,n+1):
            factorial *= i
        return factorial

def IterativeCombination(n,k):
    if n == k:
        return 1
    elif k > n:
        return 0
    else:
        return(IterativeFactorial(n)/(IterativeFactorial(k) * IterativeFactorial(n - k)))

def RecursiveCombination(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif n < k:
        return 0
    elif 2 <= k <= n:
        return(RecursiveCombination(n-1,k-1) + RecursiveCombination(n-1,k))

class Trace:
    def __init__(self):
        self.count = 0
        self.result = 0

    def GetCount(self):
        return (self.count)

    def IncrementCount(self, c):
        self.count += c

    def ResetCount(self):
        self.count = 0

    def UpdateResult(self, r):
        self.result = r

def IterativeCombinationTrace(n,k):
    CTrace = Trace()
    if n == k:
        return 1
    elif k > n:
        return 0
    else:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            factorialn,factorialk,factorialnk = 1,1,1
            for i in range(1,n+1):
                factorialn *= i
                CTrace.IncrementCount(1)
          
            for i in range(1,k+1):
                factorialk *= i
                CTrace.IncrementCount(1)
          
            for i in range(1,n-k+1):
                factorialnk *= i
                CTrace.IncrementCount(1)
          
        return (factorialn/(factorialk * factorialnk)),CTrace.GetCount()

def RecursiveCombinationObject(n,k,obj):
    obj = Trace()
    if k == 0:
        obj.IncrementCount(1)
        return 1
    elif k == 1:
        obj.IncrementCount(1)
        return n
    elif n < k:
        obj.IncrementCount(1)
        return 0
    elif 2 <= k <= n:
        return(RecursiveCombination(n-1,k-1,obj(n)) + RecursiveCombination(n-1,k,obj(n)))
    print(obj.GetCount())

#Cant get trace to work for the recursive function. Couldn't do the rest of the functions.

def PascalTriangle(n):
    for i in range(n+1):
        print(RecursiveCombination(n,i))
    
PascalTriangle(5)
