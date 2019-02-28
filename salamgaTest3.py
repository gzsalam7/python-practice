#Test 3
import math

def salamgaTest3():
    x = eval(input("Which question do you want to perform?: "))
    if x == 1:
        fibonacci()
        

def fibonacci():
    n = eval(input("Which number in the sequence do you seek?: "))
    now = 1
    last = 1
    for i in range(n-2):
        now, last = now+last, now
    print(now)

fibonacci()

def myRound():
    i = eval(input("Input an integer: "))
    f = eval(input("Input a float: "))
    print(round(f,i))
myRound()

def basicExponentiation():
    b = eval(input("What is the base: "))
    e = eval(input("What is the exponent: "))
    answer = 1
    for i in range(e):
        answer = answer*b
    print(answer)

        
    
             
