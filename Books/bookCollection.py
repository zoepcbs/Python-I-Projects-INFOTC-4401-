from Book import Book

def options():
    print("\nWhat would you like to do?")
    print("1. Add a new book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. View a book's information")
    print("5. View all books")
    print("6. Exit")


def add_new_book(collection):
    
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    
    try:
        newBook = Book(title, author, year)
        collection.append(newBook)
        
        print(f"\nBook '{title}' by {author} ({year}) added to the collection.")
        
    except ValueError as ve:
        print(f"Error adding book: {ve}")

def list_books(collection):
    if not collection:
        print("No books in the collection.")
        return
    for idx, book in enumerate(collection, start=1):
        print(f"{idx}. {book.get_title()}")

def choose_book(collection, option):

    if not collection:
        print("No books in the collection.")
        return None

    print(f"\nPlease choose a book to {option}:")
    list_books(collection)

    while True:
        choice = input("Enter the number of the book: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(collection):
                return collection[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(book_collection)}.")
        else:
            print("Invalid input. Please try again.")

def check_out_book(collection):

    book = choose_book(collection, "check out")

    if book:
        message = book.check_out()
        print(message)

def return_book(collection):
    book = choose_book(collection, "return")

    if book:
        message = book.return_book()
        print(message)

def view_book_info(collection):
    
    book = choose_book(collection, "view")
    if book:
        print("\nBook Information:")
        print(book.get_info())

def view_collection(collection):
    
    if not collection:
        print("\nNo books in the collection.")
    else:
        print("\nYour Book Collection:")
        for idx, book in enumerate(collection, start=1):
            print(f"\nBook {idx}:")
            print(book.get_info())

def exit_manager(collection):
    print("\nYour Book Collection:")
    if not collection:
        print("No books in the collection.")
    else:
        for idx, book in enumerate(collection, start=1):
            print(f"\nBook {idx}:")
            print(book.get_info())
    print("Thank you for using the book collection manager!")
    
def main():
    
    print("\nWelcome to the book collection manager!")
    print("This program lets you manage your book collection.")

    collection = []

    while True:
        options()
        choice = input("Choice: ").strip()

        if choice == '1':
            add_new_book(collection)
        elif choice == '2':
            check_out_book(collection)
        elif choice == '3':
            return_book(collection)
        elif choice == '4':
            view_book_info(collection)
        elif choice == '5':
            view_collection(collection)
        elif choice == '6':
            exit_manager(collection)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            

if __name__ == "__main__":
    main()
