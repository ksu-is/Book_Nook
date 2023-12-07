from  tkinter import *
from tkinter import ttk
from tkmacosx import Button
from views import *
from tkinter import messagebox

#colors
co0 = "#ffffff" #white
co1 = "#000000" #black
co2 = "#00868B" #purple

window = Tk()
window.title("")
window.geometry('500x500')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)



#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=180, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=200, bg=co0, relief="flat")
frame_table.grid(row=2, column=0, columnspan=6, padx=0, pady=1, sticky=NW)

#functions
def show():
    global tree

    listheader = ['Title', 'Author', 'Genre', 'Satus', 'Rating']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text="Title", anchor=NW)
    tree.heading(1, text="Author", anchor=NW)
    tree.heading(2, text="Genre", anchor=NW)
    tree.heading(3, text="Status", anchor=NW)
    tree.heading(4, text="Rating", anchor=NW)

    #tree columns
    tree.column(0, width=150, anchor=W)
    tree.column(1, width=135, anchor=W)
    tree.column(2, width=80, anchor=W)
    tree.column(3, width=80, anchor=W)
    tree.column(4, width=40, anchor=CENTER)

    for item in demo_list:
        tree.insert('','end', values=item)

show()

def insert():
    Title = e_title.get().title()
    Author = e_author.get().title()
    Genre = c_genre.get()
    Status = c_status.get()
    Rate = c_rate.get()

    data = [Title, Author, Genre, Status, Rate]
    
    if Title == '' or Author == '' or Genre == '' or Status == '' or Rate == '':
        messagebox.showwarning('data','Please fill in al fields')
    
    else:
        add(data)

        e_title.delete(0, 'end')
        e_author.delete(0, 'end')
        c_genre.delete(0, 'end')
        c_status.delete(0, 'end')
        c_rate.delete(0, 'end')

        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Title = str(tree_list[0])
        Author = str(tree_list[1])
        Genre = str(tree_list[2])
        Status = str(tree_list[3])
        Rate = str(tree_list[4])

        e_title.insert(0, Title)
        e_author.insert(0, Author)
        c_genre.insert(0, Genre)
        c_status.insert(0, Status)
        c_rate.insert(0, Rate)

        def confirm():
            new_title = e_title.get()
            new_author = e_author.get()
            new_genre = c_genre.get()
            new_status = c_status.get()
            new_rate = c_rate.get()

            data = [new_title, new_title, new_author, new_genre, new_status, new_rate]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_title.delete(0, 'end')
            e_author.delete(0, 'end')
            c_genre.delete(0, 'end')
            c_status.delete(0, 'end')
            c_rate.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()
            
            b_confirm.destroy()

            show()

        b_confirm = Button(frame_down, text="Confirm", height=25, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x=310, y=110)

    except IndexError:
        messagebox.showerror('Error', 'Select a book from table.')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_title = str(tree_list[0])

        remove(tree_title)

        messagebox.showinfo('Success', 'Book data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()
        
        show()

    except IndexError:
        messagebox.showerror('Error', 'Select a book from table.')

def to_search():
    title = e_search.get()

    data = search(title)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)

    e_search.delte(0,'end')

       
#frame_up widgets

app_name = Label(frame_up, text="BookNook", height = 1, font=('Verdana 20 bold'), bg = co2, fg = co0)
app_name.place(x=5, y=5)

#frame_down widgets
l_title = Label(frame_down, text="Title *", width=20, height=1, font=('Ivy 12 bold'), bg=co0, anchor=NW)
l_title.place(x=10, y=20)
e_title = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief="solid")
e_title.place(x=80, y=20)

l_author = Label(frame_down, text="Author *", width=20, height=1, font=('Ivy 12 bold'), bg=co0, anchor=NW)
l_author.place(x=10, y=50)
e_author = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief="solid")
e_author.place(x=80, y=50)

l_genre = Label(frame_down, text="Genre *", width=20, height=1, font=('Ivy 12 bold'), bg=co0, anchor=NW)
l_genre.place(x=10, y=80)
c_genre = ttk.Combobox(frame_down, width=19)
c_genre['values'] = ['','Fantasy','Romance','Classic','Fiction','NonFiction', 'Thriller', 'Other']
c_genre.place(x=80, y=80)

l_status = Label(frame_down, text="Status *", width=20, height=1, font=('Ivy 12 bold'), bg=co0, anchor=NW)
l_status.place(x=10, y=110)
c_status = ttk.Combobox(frame_down, width=10)
c_status['values'] = ['','not read','reading','read']
c_status.place(x=80, y=110)

l_rate = Label(frame_down, text="Rating *", width=8, height=1, font=('Ivy 12 bold'), bg=co0, anchor=NW)
l_rate.place(x=10, y=140)
c_rate = ttk.Combobox(frame_down, width=10)
c_rate['values'] = ['','NA','1','2','3','4','5']
c_rate.place(x=80, y=140)

b_search = Button(frame_down, text="Search", height=24, width=60, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=to_search)
b_search.place(x=280, y=20)
e_search = Entry(frame_down, width=20, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=350, y=20)

b_view = Button(frame_down, text="View", height=25, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=show)
b_view.place(x=310, y=50)

b_add = Button(frame_down, text="Add", height=25, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=insert)
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update", height=25, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=to_update)
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete", height=25, bg=co2, fg=co0, borderless=1, font=('Ivy 8 bold'), command=to_remove)
b_delete.place(x=400, y=110)

window.mainloop()
