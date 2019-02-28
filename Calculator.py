from tkinter import *
from tkinter import ttk
#The calculator works by itself, I managed to get it running by itself but it crashes now if a second operation is attempter
#I was not able to connect the number system, radiobuttons and the Assign function together
#I was able to get the conversion functions for the number classto work but
#they do not work with the calculator
#Isolated they do work if given an input on their own.
class Calculator:
    num1 = ""
    num2 = ""
    operation = ""
    isNum1 = True
    digitButtons = []
    operatorButtons = []
    equalsButton = []
    clearButton = []
    num1Obj = None
    num2Obj = None
    v = 10
    numberSystem = 10
    def __init__(self, master):
        mainframe = ttk.Frame(master, relief=SUNKEN, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=7, rowspan=6,sticky='NWES')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        #labelSeparator = ttk.Separator(mainframe, orient=HORIZONTAL)
        #labelSeparator.grid(row=1, rowspan=20, pady=30, sticky="EW")
        
        viewLabel = Label(mainframe, text="0")
        viewLabel.grid(row=0, column=0, columnspan=20, sticky="EW")

        oneButton = ttk.Button(mainframe, text='1', command = lambda : self.AppendDigit(1, viewLabel))
        oneButton.grid(column = 0, row = 1, pady = 5)
        self.digitButtons.append(oneButton)

        twoButton = ttk.Button(mainframe, text='2', command = lambda : self.AppendDigit(2, viewLabel))
        twoButton.grid(column = 1, row = 1, pady = 5)
        self.digitButtons.append(twoButton)

        threeButton = ttk.Button(mainframe, text='3', command = lambda : self.AppendDigit(3, viewLabel))
        threeButton.grid(column = 2, row = 1, pady = 5)
        self.digitButtons.append(threeButton)

        fourButton = ttk.Button(mainframe, text='4', command = lambda : self.AppendDigit(4, viewLabel))
        fourButton.grid(column = 0, row = 2, pady = 5)
        self.digitButtons.append(fourButton)

        fiveButton = ttk.Button(mainframe, text='5', command = lambda : self.AppendDigit(5, viewLabel))
        fiveButton.grid(column = 1, row = 2, pady = 5)
        self.digitButtons.append(fiveButton)

        sixButton = ttk.Button(mainframe, text='6', command = lambda : self.AppendDigit(6, viewLabel))
        sixButton.grid(column = 2, row = 2, pady = 5)
        self.digitButtons.append(sixButton)

        sevenButton = ttk.Button(mainframe, text='7', command = lambda : self.AppendDigit(7, viewLabel))
        sevenButton.grid(column = 0, row = 3, pady = 5)
        self.digitButtons.append(sevenButton)

        eightButton = ttk.Button(mainframe, text='8', command = lambda : self.AppendDigit(8, viewLabel))
        eightButton.grid(column = 1, row = 3, pady = 5)
        self.digitButtons.append(eightButton)

        nineButton = ttk.Button(mainframe, text='9', command = lambda : self.AppendDigit(9, viewLabel))
        nineButton.grid(column = 2, row = 3, pady = 5)
        self.digitButtons.append(nineButton)

        zeroButton = ttk.Button(mainframe, text='0', command = lambda : self.AppendDigit(0, viewLabel))
        zeroButton.grid(column = 1, row = 3, pady = 5)
        self.digitButtons.append(zeroButton)

        addButton = ttk.Button(mainframe, text='+', command = lambda : self.RecordOperator('+'))
        addButton.grid(column=3,row=1,pady=5)
        self.operatorButtons.append(addButton)
        subtractButton = ttk.Button(mainframe, text='-', command = lambda : self.RecordOperator('-'))
        subtractButton.grid(column=3,row=2,pady=5)
        self.operatorButtons.append(subtractButton)
        multiplyButton = ttk.Button(mainframe, text='*', command = lambda : self.RecordOperator('*'))
        multiplyButton.grid(column=3,row=3,pady=5)
        self.operatorButtons.append(multiplyButton)
        divideButton = ttk.Button(mainframe, text='//', command = lambda : self.RecordOperator('//'))
        divideButton.grid(column=3,row=4,pady=5)
        self.operatorButtons.append(divideButton)

        equalsButton = ttk.Button(mainframe, text='=', command = lambda : self.ComputeResult(viewLabel))
        equalsButton.grid(column=4, row=2, pady=5)
        self.equalsButton.append(equalsButton)

        clearButton = ttk.Button(mainframe, text="Clear", command = lambda : self.ClearAll(viewLabel))
        clearButton.grid(column=4, row=3, pady=5)
        self.clearButton.append(clearButton)

        dbutton = ttk.Radiobutton(mainframe, text="Decimal", variable=self.v, value=10, command=self.AssignSystem(self.numberSystem, viewLabel),  takefocus=False)
        dbutton.grid(row=0,column=4)
        bbutton = ttk.Radiobutton(mainframe, text="Binary", variable=self.v, value=2, command=self.AssignSystem(self.numberSystem, viewLabel),takefocus=False)
        bbutton.grid(row=1,column=4)
        

        self.DisableButtons(self.operatorButtons + self.equalsButton + self.clearButton)

        return

    def AppendDigit(self, digit, viewLabel):
        if(self.isNum1):
            self.num1 = self.num1 + str(digit)
            viewLabel.config(text = self.num1)
            self.EnableButtons(self.operatorButtons + self.clearButton)
        else:
            self.num2 = self.num2 + str(digit)
            viewLabel.config(text = self.num2)
            self.EnableButtons(self.equalsButton)

        return

    def RecordOperator(self, op):
        self.operation = op
        num1Obj = None
        num1Obj = Number(self.numberSystem,self.num1)
        #print(num1Obj.binary,num1Obj.numStr)
        self.isNum1 = False
        self.DisableButtons(self.operatorButtons)
        self.EnableButtons(self.digitButtons)

        return

    def ComputeResult(self, viewLabel):
        if(self.operation == "+"):
            r = str(int(self.num1) + int(self.num2))
            q = ""
        elif(self.operation == "-"):
            r = str(int(self.num1) - int(self.num2))
            q = ""
        elif(self.operation == "*"):
            r = str(int(self.num1) * int(self.num2))
            q = ""
        elif(self.operation == "//"):
            r = str(int(self.num1) // int(self.num2))
            q = "R" + str(int(self.num1) % int(self.num2))

        viewLabel.config(text = (r+q))

        self.EnableButtons(self.operatorButtons)
        self.DisableButtons(self.digitButtons + self.equalsButton)

        self.num1 = r
        self.num2 =""
        self.isNum1 = True

        return

    def ClearAll(self, viewLabel):
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        isNum1 = True
        num1Obj = None
        num2Obj = None

        self.EnableButtons(self.digitButtons)
        self.DisableButtons(self.operatorButtons + self.equalsButton + self.clearButton)

        viewLabel.config(text = "")

        return

    def EnableButtons(self, bList):
        for i in bList:
            i.config(state = NORMAL)
        return

    def DisableButtons(self, bList):
        for i in bList:
            i.config(state = DISABLED)
        return

    def AssignSystem(self, base, viewLabel):
        pass
            
class Number:
    binary = 0
    decimal = 0
    def __init__(self, base, numStr):
        self.base, self.numStr = base, numStr
        if self.numStr == "":
            self.numStr = 0
        if self.base == 2:
            self.binary = self.numStr
            self.decimal = self.BinaryToDecimal()
        elif self.base == 10:
            self.decimal = self.numStr
            self.binary = self.DecimalToBinary()

    def GetBinary(self):
        return self.binary

    def GetDecimal(self):
        return self.decimal

    def BinaryToDecimal(self):
        self.b = (str(self.binary)[::-1])
        power = 0
        for i in self.b:
            self.decimal += int(i)*(2**power)
            power +=1
        return self.decimal
        print(self.decimal, self.binary)
        

    def DecimalToBinary(self):
        self.dec = ""
        self.d = self.numStr
        while self.d != 0:
            self.d,self.r = int(self.d)//2,int(self.d)%2
            self.dec += str(self.r)
        self.binary = self.dec[::-1]
         
def main():
    master = Tk()

    Calculator(master)

    master.title("Calculator")
    master.mainloop()

if __name__ == main():
    main()
    
