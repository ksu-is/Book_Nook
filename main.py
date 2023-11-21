#This is the code I will be adding and editing as I work on my project
#As of right now I am running and testing most of my code on Jupyter

reading_list = []
menu_prompt = """Welcome to Book_Nook! Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

#would like to add 'genre' and 'page count' options
def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    #dictionary
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    
    reading_list.append(new_book)
    
def show_books():
    for book in reading_list:
        print(f"{book['title']}, by {book['author']} ({book['year']})")


while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        show_book()
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")
        
    selected_option = input(menu_prompt).strip().lower()
