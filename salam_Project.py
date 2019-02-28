
#Imports the relevant packages, the last two imports are for message boxes
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#This class creates the manager and holds all the data
class InventoryManager:

    def __init__(self, master):
        mainframe = ttk.Frame(master, relief=SUNKEN, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=7, rowspan=8,sticky='NWES')
        #Updates the frame so it does not freeze after loading data and creates an Item class that holds the inventory
        mainframe.update()
        self.inv = Item()
        #Creates the item fields and labels
        self.numberLabel = Label(mainframe, text="Item Number")
        self.numberLabel.grid(row=0, column=0)
        self.numberEntry = Entry(mainframe)
        self.numberEntry.grid(row=0, column=1)
        self.quantityLabel = Label(mainframe, text="Quantity")
        self.quantityLabel.grid(row=1, column=0)
        self.quantityEntry = Entry(mainframe)
        self.quantityEntry.grid(row=1, column=1)
        self.nameLabel = Label(mainframe, text="Name")
        self.nameLabel.grid(row=2, column=0)
        self.nameEntry = Entry(mainframe)
        self.nameEntry.grid(row=2, column=1)
        self.locationLabel = Label(mainframe, text="Item Location")
        self.locationLabel.grid(row=3, column=0)
        self.locationEntry = Entry(mainframe)
        self.locationEntry.grid(row=3, column=1)
        self.descriptionLabel = Label(mainframe, text="Item Description")
        self.descriptionLabel.grid(row=4, column=0)
        self.descriptionEntry = Entry(mainframe)
        self.descriptionEntry.grid(row=4, column=1)

        #creates the box to display all the inventory records
        self.inventoryBox = Text(mainframe, height=10, width=100)
        self.inventoryBox.grid(row=0, column=2, rowspan=5, padx=8, pady=8, sticky='S')

        #creates buttons for each function to be performed and entries for the item number to perform on
        self.newButton = ttk.Button(mainframe, command= lambda: self.addEntry(), text="New")
        self.newButton.grid(row=5, column=1, pady=8)
        self.deleteButton = ttk.Button(mainframe, command=lambda: self.delete(), text="Delete")
        self.deleteButton.grid(row=6, column=0)
        self.deleteEntry = Entry(mainframe)
        self.deleteEntry.grid(row=6, column=1)
        self.searchButton = ttk.Button(mainframe,command=lambda: self.search(), text="Search")
        self.searchButton.grid(row=7,column=0)
        self.searchEntry = Entry(mainframe)
        self.searchEntry.grid(row=7,column=1)
        self.updateButton = ttk.Button(mainframe, command=lambda: self.update(), text="Update")
        self.updateButton.grid(row=8, column=0)

        self.loadButton = ttk.Button(mainframe, command=lambda: self.loadData(), text="Load")
        self.loadButton.grid(row=5, column=2)

        self.saveButton = ttk.Button(mainframe, command=lambda: self.inv.saveData(),text="Save")
        self.saveButton.grid(row=6, column=2)

    #Add function, takes input from the entry boxes and creates a new inventory record
    def addEntry(self):
        #checks input from entries is not emptry string
        for i in self.inv.inventory:
            assert i[0] != self.numberEntry.get(),messagebox.showinfo("Entry Error","Item number already exists")
        assert self.nameEntry.get() != "",messagebox.showinfo("Entry Error","Name entry is empty")
        assert self.locationEntry.get() != "",messagebox.showinfo("Entry Error","Location entry is empty")
        assert self.descriptionEntry.get() != "",messagebox.showinfo("Entry Error","Description entry is empty")
        #first checks that item number and quantity are positive integers
        try:
            int(self.numberEntry.get()) == int
            int(self.quantityEntry.get()) == int
            int(self.numberEntry.get()) >= 0
            int(self.quantityEntry.get()) >= 0
            #appends the new entry to the item inventory record
            self.inv.inventory.append([self.numberEntry.get(),self.quantityEntry.get(),
                                   self.nameEntry.get(), self.locationEntry.get(),
                                   self.descriptionEntry.get()])
            #sorts the list after loading from the records using the first entry of the list converted to an int
            self.inv.inventory = sorted(self.inv.inventory, key=lambda x: int(x[0]))
            #refreshes the inventory box to show accurate records
            self.refreshInventory()
        #errorbox to catch incorrect quantity and number entries
        except:
            messagebox.showinfo("Entry Error","Item number and Quantity must be a number")

    #search function that runs through the inventory and matches to search entry field
    def search(self):
        #counter that opens message box if the search match of the search entry fails
        self.searchCount = False
        for i in self.inv.inventory:
            #if statement matches the search entry field to the number record of each item
            if i[0] == self.searchEntry.get():
                #sets counter to true so messagebox does not go off
                self.searchCount = True
                self.numberEntry.delete(0,END)
                self.numberEntry.insert(0,i[0])
                self.quantityEntry.delete(0,END)
                self.quantityEntry.insert(0,i[1])
                self.nameEntry.delete(0,END)
                self.nameEntry.insert(0,i[2])
                self.locationEntry.delete(0,END)
                self.locationEntry.insert(0,i[3])
                self.descriptionEntry.delete(0,END)
                self.descriptionEntry.insert(0,i[4])
        #checks the searchCount for false if the search fails and warns the user
        if self.searchCount == False:
            messagebox.showinfo("Search Failed","Item Number not found")

    #function for the update button to change an item record
    def update(self):
        #updateCounter to check if the update search found the item to update
        self.updateCount = False
        #searches through the item records and compares the item number to the number record
        for i in self.inv.inventory:
            if i[0] == self.numberEntry.get():
                #checks the entry field for the correct inputs and throws messagebox if they are wrong
                try:
                    int(self.numberEntry.get()) == int
                    int(self.quantityEntry.get()) == int
                    int(self.numberEntry.get()) >= 0
                    int(self.quantityEntry.get()) >= 0
                    assert self.nameEntry.get() != "",messagebox.showinfo("Entry Error","Name entry is empty")
                    assert self.locationEntry.get() != "",messagebox.showinfo("Entry Error","Location entry is empty")
                    assert self.descriptionEntry.get() != "",messagebox.showinfo("Entry Error","Description entry is empty")
                    self.updateCount = True
                    i[1] = self.quantityEntry.get()
                    i[2] = self.nameEntry.get()
                    i[3] = self.locationEntry.get()
                    i[4] = self.descriptionEntry.get()
                    self.refreshInventory()
                except:
                    messagebox.showinfo("Entry Error","Item number and Quantity must be a number")
                    self.updateCount = True
        if self.updateCount == False:
            messagebox.showinfo("Update Failed","Item Number Not Found")
        self.inv.inventory = sorted(self.inv.inventory, key=lambda x: int(x[0]))

    #delete function that deletes the item in the delete entry field
    def delete(self):
        #counter that checks the item that is in the entry exists
        self.deleteCount = False
        #searches delete entry field for the item inputted
        for i in self.inv.inventory:
            if i[0] == self.deleteEntry.get():
                self.deleteCount = True
                #opens a confirmation dialog box and saves the answer as result variable
                result = messagebox.askquestion("Delete", "Confirm Deletetion?", icon='warning')
                #if result is yes then deletes the item from inventory and refreshes the inventory box to show this
                if result == 'yes':
                    self.inv.inventory.remove(i)
                    self.refreshInventory()
                ##if no button is clicked then the function stops
                else:
                   break
        #Opens dialog box if the delete entry doesnt exist
        if self.deleteCount == False:
            messagebox.showinfo("Not Found","Item number not found")

    #function refreshes the inventorybox after loading from a file
    def loadData(self):
        self.inv.loadData()
        self.refreshInventory()

    #Refreshes the inventroybox to show the stored records
    def refreshInventory(self):
        #deletes the current contents of the inventoryBox so it can be rewritten
        self.inventoryBox.delete('1.0', END)
        #first for loop runs through the lists in the list
        for i in self.inv.inventory:
            #second for loop runs through each part of the items properties so it can be displayed
            for j in i:
                #inserts a line between the item properties to sepereater them
                self.inventoryBox.insert(INSERT, j + " | ")
            #creates each item on a new line to easier seperate them
            self.inventoryBox.insert(INSERT, "\n")

#creates item class that helps save the inventory record for the manager
class Item:
    def __init__(self):
        #opens an inventory and a new inventory which helps load and save the items entered
        self.inventory = []
        self.newInventory = []

    def loadData(self):
        #checks if file is a text file
        try:
            #opens dialog box to open record from
            filePath = filedialog.askopenfilename()
            file = open(filePath,"r")
            for line in file:
                #removes the line characrer at the end and splits the item at the commas between each item property
                line = line.strip('\n')
                line = line.split(',')
                #adds 
                self.newInventory.append(line)
            #sorts the new inventory into the inventory
            self.inventory = sorted(self.newInventory, key=lambda x: int(x[0]))
            #adds the new inventory into the working inventory
            self.newInventory = []
            file.close()
        except:
            messagebox.showinfo("Load Error","File selected was not a text file")

    #save function to store the inventory record into a text file
    def saveData(self):
        #counter to make sure comma isn't added to the end of a line in the record which can cause issues
        self.count = 0
        filePath = filedialog.asksaveasfile(mode='w',title="Select a text file to save to",
                defaultextension=".txt")
        #for each item in the inventory
        for i in self.inventory:
            #splits the item into individual properties
            for j in i:
                filePath.write(j)
                #adds comma to inbetween each property except for the last one
                if self.count != 4:
                    filePath.write(',')
                    self.count+=1
            #adds newline between each item to seperate them
            filePath.write('\n')
            self.count = 0
        filePath.close()

#runs the program when the file is clicked
def main():
    master = Tk()

    InventoryManager(master)

    master.title("Inventory Manager")
    master.mainloop()


if __name__ == main():
    main()
