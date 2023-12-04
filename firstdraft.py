#This is the code I will be adding and editing as I work on my project
#As of right now I am running and testing most of my code on Jupyter
#Update: I have transferred to my work from Jupyter to Visual Studio Code and started using csv files


menu_prompt = """Welcome to Book_Nook! Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

#would like to add 'genre' and 'page count' options
def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    #open in append mode
    with open("book.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year}\n")
    
#find books in database 
def get_all_books():
    books = []

    with open("books.csv","r") as reading_list:
        for book in reading_list:
            title, author, year = book.strip().split(",")
            #create dictionary with information and put into books variable
            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books
    
def show_books(books):
    print()
    
    for book in books:
        title, author, year = book.values()
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    
    print()

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Enter a book title to search for: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books
    
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        reading_list = get_all_books()
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
        #printing message if reading list is empty rather than just appearing blank. 
    elif selected_option == "s":
        matching_books = find_books()

        if matching_books:
            show_books(matching_books)
        else:("Sorry, no books found matching that search term.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")
        
    selected_option = input(menu_prompt).strip().lower()
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")
        
    selected_option = input(menu_prompt).strip().lower()
