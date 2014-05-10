

#invoked when search button pressed
def search():
    pass

#invoked when key1 button pressed
def key1():
    pass

#invoked when key2 button pressed
def key2():
    pass

#invoked when key3 button pressed
def key3():
    pass


from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Emotions of the keywords")

#label
label=ttk.Label(root, text="Emotions of the keywords")

searchText = StringVar()
# search box
searchEntry = ttk.Entry(root, width=50, textvariable=searchText)

# search button
searchButton=ttk.Button(root, text="Search", command=search)


keyFrame=Frame(root)
# key1 button
key1Button=ttk.Button(keyFrame, text="Key1", command=key1)
# key2 button
key2Button=ttk.Button(keyFrame, text="Key2", command=key2)
# key3 button
key3Button=ttk.Button(keyFrame,text="Key3", command=key3)
# key1Button=ttk.Button(root, text="Key1", command=key1)
# key2Button=ttk.Button(root, text="Key2", command=key2)
# key3Button=ttk.Button(root,text="Key3", command=key3)

# map area
convas=Canvas(root,bd=4,bg='blue')

# set layout
root.grid()
label.grid(row=0,column=1)
searchEntry.grid(row=1,column=1,sticky=W)
searchButton.grid(row=1,column=10)
keyFrame.grid(row=2,column=1)
key1Button.grid(row=2,column=0,sticky=W)
key2Button.grid(row=2,column=1)
key3Button.grid(row=2,column=2,sticky=E)
convas.grid(row=3,column=1)
root.mainloop()
if __name__ == '__main__':
    pass