#Question 2 Test 2

def salamSwapCase():
#defines function
    x = input("Enter a string: ")
    #asks for the input string
    y = []
    #creates empty list y
    for i in list(x):
    #runs through each character in x which has been turned into a list
        if i.lower() == i:
        #Looks for lowercase letters
            y.append(i.upper())
            #Capatilizes lowercase letters
        else:
        #if letter isnt lowercase
            y.append(i.lower())
            #lowercases the capital letter
    print("".join(y))
    #prints the list y which has been added to an empty string

salamSwapCase()
#calls function
