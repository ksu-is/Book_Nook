#This is the code I will be adding and editing as I work on my project
#As of right now I am running and testing most of my code on Jupyter

reading_list = []
menu_prompt = """Welcome to Book_Nook! Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

while selected_option != "q":
    if selected_option == "a":
        print("Adding...")
    elif selected_option == "l":
        print("Displaying...")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")
        
    selected_option = input(menu_prompt).strip().lower()
