import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


openfile = open(file_path,'r')
numbers = []
for i in openfile.readlines():
    numbers.append(int(i))

def location(n):
    counter = 0
    for i in numbers:
        if i == n:
            counter += 1
            print(counter)
        else:
            counter+=1

location(2)
