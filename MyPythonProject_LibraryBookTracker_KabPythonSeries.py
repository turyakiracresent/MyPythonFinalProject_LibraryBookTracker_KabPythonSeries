"""My Python final project_Library Book Tracker_KabPython Series
TURYAKIRA CRESENT 
"""

class Book:
    #Represents a book in the library.
    
    def __init__(self, title, author):
        self.title = title #title of the book
        self.author = author #author of the book
        self.is_checked_out = False # if a book is checked

    def __str__(self):
        #Return a string representation of the book.
        return f'"{self.title}" by {self.author}'

class Library:
    #Class library Manages the library collection and operations.

    def __init__(self):
        #Initializing an empty library using a list to store books
        self.books = []

    def add_book(self, book):
        #Adding  a book to the library
        self.books.append(book)
        print(f"The Book has been added: {book}")
#checking out a book from the library
    def check_out_book(self, title):
        #Checking  out a book if its available
        for book in self.books:
            if book.title == title:
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f"The has been Book checked out already: {book}")
                    return
                else:
                    print(f"The Book has been already checked out: {book}")
                    return
        print(f"The  Book has  not found: '{title}'")
        #returning a book
    def return_book(self, title):
        #Returning  a checked-out book
        for book in self.books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"The Book has been returned: {book}")
                    return
                else:
                    print(f"The Book was not checked out: {book}")
                    return
        print(f"The Book has  not been found: '{title}'")

    def display_available_books(self):
        #Displaying  all the available books (When a book is not checked out).
        available_books = [book for book in self.books if not book.is_checked_out]
        if available_books:
            print("The Available Books In The library Are: ")
            for book in available_books:
                print(book)
        else:
            print("Oh! Sorry. There Are No Available books in the library yet")

def main():
    # Creating a variable for class Library(instance of a library class)
    library = Library()
#Using a while loop to display a libary menu
    while True:
        print("\nChoose An Option From The Library Menu Displayed Below:")
        print("1. Add A Book To The Library.")
        print("2. Check Out A Book In The Library.")
        print("3. Return A Book To The Library.")
        print("4. Display All The  Available Books In The Library.")
        print("5.  \"Choose This Option To Exit Our Library Book Tracker System.\"")

        choice = input("Enter Your Choice [1-5]: ")

        if choice == '1':
            title = input("Enter The Book Title: ")
            author = input("Enter The Author Of The Book: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            title = input("Enter The Book Title To Check Out: ")
            library.check_out_book(title)
        elif choice == '3':
            title = input("Enter The Book Title To Return: ")
            library.return_book(title)
        elif choice == '4':
            library.display_available_books()
        elif choice == '5':
            print("Your Have Exited The Program. Thanks For Visiting Our Library Book Tracker.")
            print("\n You Will Be Welcome Once Again You Decide To Visit Us. Thank You.")
            break
        else:
            print("You Have Entered An Invalid choice. Please Try Again.")

if __name__ == "__main__":
    """
            checks if the script is being run directly(not imported as a module in another script)
    """
    #calling the main function
    main()