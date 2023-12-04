#I will be using tkinter to create my BookNook Program

from  tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff" #white
co1 = "#000000" #black
co2 = "#A43B76" #purple

window = Tk()
window.title("")
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)

#frame_up widgets

app_name = Label(frame_up, text="BookNook", height = 1, font=('Verdana 17 bold'), bg = co2, fg = co0)
app_name.place(x=5, y=5)

#frame_down widgets
l_title = Label(frame_down, text="Title *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_title.place(x=10, y=20)
e_title = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_title.place(x=80, y=20)

l_author = Label(frame_down, text="Author *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_author.place(x=10, y=50)
e_author = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_author.place(x=80, y=50)

l_genre = Label(frame_down, text="Genre *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_genre.place(x=10, y=80)
c_genre = ttk.Combobox(frame_down, width=23)
c_genre['values'] = ['','Fantasy','Romance','Classic','Fiction','NonFiction','Other']
c_genre.place(x=80, y=80)

l_status = Label(frame_down, text="Status *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_status.place(x=10, y=110)
c_status = ttk.Combobox(frame_down, width=10)
c_status['values'] = ['','not read','reading','read']
c_status.place(x=80, y=110)

l_rate = Label(frame_down, text="Rating *", width=8, height=1, font=('Ivy 10'), bg=co0,)
l_rate.place(x=195, y=110)
c_rate = ttk.Combobox(frame_down, width=4)
c_rate['values'] = ['','1','2','3','4','5']
c_rate.place(x=250, y=110)

window.mainloop()
