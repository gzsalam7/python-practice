def pointDistance():
    x1 = eval(input("Input first points x value: "))
    y1 = eval(input("Input first points y value: "))
    x2 = eval(input("Input second points x value: "))
    y2 = eval(input("Input second points y value: "))
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(distance)
pointDistance()
