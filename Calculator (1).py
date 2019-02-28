from tkinter import *
from tkinter import ttk

class Calculator:
    num1 = ""
    num2 = ""
    operation = ""
    isNum1 = True
    digitButtons = []
    operatorButtons = []
    equalsButton = []
    clearButton = []
    def __init__(self, master):
        mainframe = ttk.Frame(master, relief=SUNKEN, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=7, rowspan=6,sticky='NWES')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        calculation = StringVar()
        viewLabel = Label(mainframe, text="asd")
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

        addButton = ttk.Button(mainframe, text='+', command = lambda : RecordOperator('+'))
        addButton.grid(column=3,row=1,pady=5)
        self.operatorButtons.append(addButton)
        subtractButton = ttk.Button(mainframe, text='-', command = lambda : RecordOperator('-'))
        subtractButton.grid(column=3,row=2,pady=5)
        self.operatorButtons.append(subtractButton)
        multiplyButton = ttk.Button(mainframe, text='*', command = lambda : RecordOperator('*'))
        multiplyButton.grid(column=3,row=3,pady=5)
        self.operatorButtons.append(multiplyButton)
        divideButton = ttk.Button(mainframe, text='//', command = lambda : RecordOperator('//'))
        divideButton.grid(column=3,row=4,pady=5)
        self.operatorButtons.append(divideButton)

        equalsButton = ttk.Button(mainframe, text='=', command = lambda : ComputeResult(viewLabel))

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
        self.isNum1 = False
        self.DisableButtons(operatorButtons)
        self.EnableButtons(digitButtons)

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
        elif(Self.operation == "//"):
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
            
        
def main():
    master = Tk()

    Calculator(master)

    master.title("Calculator")
    master.mainloop()

if __name__ == main():
    main()
    
