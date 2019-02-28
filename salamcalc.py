#Question 3 Test 2

def salamcalc():
#creates the function for it to be able to run
    print("Welcome to SalamCalc!")
    operator = input("What operation do you wish to perform?:" )
    #takes the input operator and stores as variable operator
    x1 = input("What is the first number you wish to perform it on?: ")
    #asks for first number and stores as variable x1
    x2 = input("What is the second number you wish to perform it on?: ")
    #asks for the second number and stores as variable x2
    print(x1, operator, x2, "= ", eval(x1 + operator + x2))
    #prints the variables and the operator and then evauluates them right after
    print("Thanks for using SalamCalc!")

#salamcalc()
