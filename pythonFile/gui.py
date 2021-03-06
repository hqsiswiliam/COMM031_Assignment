from Tkinter import *
import ttk
import pickle
import twitter_trends
import load_test
world_trends_search_keyword = twitter_trends.search_queries_in_trends_world()

# world_trends_search_keyword = ['a','b','c']

#invoked when search button pressed
def search():
	print searchEntry.get()
	if searchEntry.get()=="":
		status_text.set("Please enter keyword")
	status_text.set("Loading keywords' list")
	lists = twitter_trends.queries_for_keyword(searchEntry.get())
	print lists
	status_text.set("predicting")
	percentage_list = load_test.predictTheResult(lists)
	print percentage_list
	initial = 0
	red_area = 360*percentage_list[0]
	blue_area = 360*percentage_list[1]
	green_area = 360*percentage_list[2]
	purple_area = 360*percentage_list[3]
	orange_area = 360*percentage_list[4]
	snow_area = 360*percentage_list[5]
	status_text.set("drawing")
	convas.create_arc(coord, fill="red", start=0, extent = red_area)
	convas.create_arc(coord, fill="blue", start=red_area, extent =blue_area)
	convas.create_arc(coord, fill="green", start=red_area+blue_area, extent =green_area)
	convas.create_arc(coord, fill='purple', start=red_area+blue_area+green_area, extent =purple_area)
	convas.create_arc(coord, fill="orange", start=red_area+blue_area+green_area+purple_area, extent = orange_area)
	convas.create_arc(coord, fill="snow", start=red_area+blue_area+green_area+purple_area+orange_area, extent = snow_area)
	status_text.set("done")
#invoked when key1 button pressed
def key1():
    searchEntry.delete(0,END)
    searchEntry.insert(0,world_trends_search_keyword[0])

#invoked when key2 button pressed
def key2():
    searchEntry.delete(0,END)
    searchEntry.insert(0,world_trends_search_keyword[1])

#invoked when key3 button pressed
def key3():
    searchEntry.delete(0,END)
    searchEntry.insert(0,world_trends_search_keyword[2])


print 'hello world'


root = Tk()
root.title("Emotions of the keywords")

#label
status_text = StringVar()
label=ttk.Label(root, text="Emotions of the keywords")
statusLabel= ttk.Label(root, textvariable=status_text)
status_text.set("####Status####")
searchText = StringVar()
# search box
searchEntry = ttk.Entry(root, width=50, textvariable=searchText)

# search button
searchButton=ttk.Button(root, text="Search", command=search)


keyFrame=Frame(root)
# key1 button
key1Button=ttk.Button(keyFrame, text=world_trends_search_keyword[0].replace("%23","#"), command=key1)
# key2 button
key2Button=ttk.Button(keyFrame, text=world_trends_search_keyword[1].replace("%23","#"), command=key2)
# key3 button
key3Button=ttk.Button(keyFrame,text=world_trends_search_keyword[2].replace("%23","#"), command=key3)
# key1Button=ttk.Button(root, text="Key1", command=key1)
# key2Button=ttk.Button(root, text="Key2", command=key2)
# key3Button=ttk.Button(root,text="Key3", command=key3)

# map area
convas=Canvas(root,bd=4,bg='white')
coord=(30,10,230,200)
convas.create_arc(coord, fill="grey", start=0, extent = 359.99999,style='chord')

# set layout
root.grid()
label.grid(row=0,column=1)
searchEntry.grid(row=1,column=1,sticky=W)
searchButton.grid(row=1,column=3)
keyFrame.grid(row=2,column=1)
key1Button.grid(row=2,column=0,sticky=W)
key2Button.grid(row=2,column=1)
key3Button.grid(row=2,column=2,sticky=E)
statusLabel.grid(row=2,column=3)
convas.grid(row=3,column=1)
#176x199 image
root.mainloop()
if __name__ == '__main__':
    pass