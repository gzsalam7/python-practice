#Test1Salam
#Part a
#prints the strings 3 and 4 together
print("3""4")

#Part b
#prints out the string 3+4= and evaluates 3+4
print("3+4 =",3+4)

#Part c
#prints the evaluation of 3*4, 3**4
print(3*4,3**4)

#Part d
#prints the evaluation of 3.44/5.66 and 6.77/2.363
print(3.44/5.66,6.77/2.363)

#Part e
print ("{0:0.6f}".format(3.44/5.66),"{0:0.6f}".format(6.77/2.363))
#prints the formatted values with precision 6

      
import math
#imports the math module
def sineloop():
#creates the function sineloop
    for i in range(21):
    #loops through values from 0-20
        print(math.sin(i))
        #prints the function of sine using the values from 0-20

sineloop()
#calls the sineloop function when the program is run
def lengthname():
#creates the lengthname function
    x = input("What is your name?")
    #asks for an input
    print(len(x))
    #prints the length of the previous input

lengthname()
#calls the lengthname function when program is run

def chaos():
#creates the chaos function
    x = eval(input("Enter number between 0 and 1: "))
    #asks for an input for x
    y = eval(input("Enter another number between 0 and 1: "))
    #asks for an input for y
    print("input","   ",x,"  ",y)
    #prints heading of table
    print("----------------------------")
    #prints divivder line
    for i in range(10):
    #loops through 0 to 9
             x = 3.9 * x * (1-x)
             #applies this function to the number and assigns its value to x
             y = 3.9 * y * (1-y)
             #applies this function to the number and assigns its value to y
             print("       ","{0:1.5f}".format(x),"{0:1.5f}".format(y))
             #prints out the value and formats it

chaos()
#Calls the chaos function

    
