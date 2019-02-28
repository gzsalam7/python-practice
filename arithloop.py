def arithloop():
    arithmatic =  ["+", "-", "*", "/"]
    x1 = input("x1? ")
    x2 = input("x2? ")
    for i in arithmatic:
        print(eval(x1 + i + x2))
    

arithloop()
