#Test 3
import math

def salamTest3():
    x = 1
    while x != 4:
        x = eval(input("Which question do you want to perform?. Input 4 to exit: "))
        if x == 1:
            print(fibonacci())
        elif x == 2:
            print(myRound())
        elif x == 3:
            print(basicExponentiation())
        else:
            print("")

def fibonacci():
    n = eval(input("Which number in the fibonacci sequence do you seek?: "))
    now = 1
    last = 1
    for i in range(n-2):
        now, last = now+last, now
    print(now)

def myRound():
    i = eval(input("Input an integer: "))
    f = eval(input("Input a float: "))
    print(round(f,i))
    print(int(f))

def basicExponentiation():
    b = eval(input("What is the base: "))
    e = eval(input("What is the exponent: "))
    answer = 1
    for i in range(e):
        answer = answer*b
    print(answer)

def main():
    print(salamTest3())

main()
    
             
