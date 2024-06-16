'''
OBJECTIVES:
    1) The project will fetch a opensource map from tkintermapview which run OpenStreetMap in the background.
    2) Secondly, the objective is to focus to update map on user search query.
'''
#Importing necessary GUI libraries 
import tkinter #Builtin
from tkinter import ttk
from countryinfo import CountryInfo
import tkintermapview #Custom library. Courtesy by TomSchimansky from Github


#Creating the widget window
window = tkinter.Tk()    
#Setting window size according to my screen size (17 inch)
window.geometry("1500x820")
cnt = tkinter.StringVar()





def search(): #This function enables users to search for the country
    country = CountryInfo(cnt.get()) #This command is fetching country info and storing it in variable to be called later on.
    cpt = country.capital() #getting country capital through country info stored in country variable
    name = country.name() #getting country name through country info stored in country variable
    tv.insert('', 'end',value=(name,cpt)) #inserting a treeview box in which the country name and capital columns are created
    map_widget.set_address(cpt, marker = True) #Updating map address and linking it with country capital.

def assigning_titles():
    #Assigning Title to the widget window
    window.title("Mudabrify")
    
    #Assigning Title to the Map
    name_label = tkinter.Label(window, text = "Mudabbrify Maps", font = ("Times New Roman", 30, "bold"))
    name_label.place(x=560, y=10, height=50, width=350)
    
    #Assigning Dedication for this project 
    dedication_label = tkinter.Label(window, text = "Dedicated to Mudassar Hassan", font = ("Times New Roman", 12, "bold", "italic"))
    dedication_label.place(x=550, y = 780, height = 50, width = 1450/4)
    
    #Dedicating this project to Stanford Code in Place
    stanford_dedication = tkinter.Label(window, text = "Stanford: Code in Place Final Project by Mudabbir Hassan")
    stanford_dedication.place(x=540, y = 60, height = 30, width = 400)
    
cnt1 = tkinter.LabelFrame(window,text ='Countries') #creating country search box
cnt1.pack(padx=100,pady=150)
cnt1.place(x=170, y = 100, height = 100, width = 300)
lbl = ttk.LabelFrame(cnt1, text = "Country Name") #Creating a label frame widget which will display country name
lbl.pack(padx=10, pady=10, side=tkinter.LEFT)
    
ent = ttk.Entry(cnt1,textvariable=cnt) #this command enables user to enter country name in cnt1 (Countries frame)
ent.pack(side=tkinter.LEFT,padx=40, pady=10)
btn = tkinter.Button(cnt1, text = 'Search', command=search) #In this command, a search button is created which is linked with search function to update map
btn.pack(side=tkinter.LEFT, padx=10, pady=10)
cnt2 = tkinter.LabelFrame(window,text='Your Search History') #Here another frame widget is created which shows search history
    
cnt2.place(x=25, y = 220, height = 260, width = 600)
tv = ttk.Treeview(cnt2, columns=(1,2), show='headings', height=10) #the search history variable cnt2 is linked with treeview which shows country info in columns
tv.pack(padx=20, pady=20)
tv.heading(1, text='Name')
tv.heading(2, text='Capital')

#Setting About window
about = tkinter.LabelFrame(window,text='About')
about.place(x=650, y = 220, height = 260, width = 800)
text = tkinter.Label(about, text="- As part of the final project for the Stanford Code in Place course, I am developing \n an interactive map application utilizing the Python Tkinter library. This application \n allows users to search for a country, upon which the map, (powered by the \n OpenStreetMap API through the tkintermapview custom library) dynamically \n updates to display the capital of the selected country.",font = 10, anchor='e')
text1 = tkinter.Label(about, text="- This project is dedicated to my brother, Mudassar Hassan, whose unwavering \n support has been instrumental in my personal and professional growth.",font = 8)
text2 = tkinter.Label(about,text="- I extend my heartfelt gratitude to Stanford University for providing me \n with this invaluable opportunity to enhance my programming skills.", font = 5)
text.pack()
text1.pack()
text2.pack()

#Creating map inside widget window by using tkintermapview
#During creating map widget we will pass the widget window variable that is window argument in TkinterMapView Class
map_widget = tkintermapview.TkinterMapView(window, width=1450, height=350,corner_radius=40)
map_widget.place(relx=0.5, rely = 0.6, anchor='n')
    
#Setting the map widget Position to Islamabad, Pakistan region through .set_position method
map_widget.set_position(33.738045, 73.084488, marker = True) #Set to Islamabad
    
#setting Zoom level of map
map_widget.set_zoom(12)
assigning_titles()   
window.mainloop()