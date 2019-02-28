#Wasnt able top finish
def main():
    sumList(toNumbers(list(salamTest5())))
    
    

def salamTest5():
    x = (input("Please enter a list of integers: "))
    return (x)
    
def squareEach(nums):
    counter = 0
    for i in nums:
        nums[counter] = i**2
        counter+= 1
    print(nums)

def sumList(nums):
    total = 0
    for i in nums:
        total += i
    return total

def toNumbers(strList):
    counter = 0
    for i in strList:
        strList[counter] = int(i)
        counter += 1
    print(strList)

def numberTest(number):
    if number % 3 == 0:
        return number
    elif  number % 5 == 0 and number % 7 == 0:
        return (number * 1000)
    elif number % 5 == 0:
        return (number * 10)
    elif number % 7 == 0:
        return (number * 100)
    else:
        return 0
    print(number)

main()

    

    
