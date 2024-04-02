"""
Online Bookstore Management System: 
"""


class Bookstore:
    def __init__(self) -> None:
        self.invetory = {}
        self.sales = []

    def add_items(self):
        isbn = input("Enter ISBN of the book to add: ")
        if isbn not in self.invetory.keys():
            details = {}
            details["Name"] = input("Enter name of the book: ").title()
            details["Author"] = input("Enter name of the author: ").title()
            details["Price"] = float(input("Enter price of the book: "))
            details["Quantity"] = float(input("Enter quantity of the book: "))
            self.invetory[isbn] = details
            print("Book added successfully!")
        else:
            print("Book already exists.")
            print(self.invetory[isbn])

    def searchBook(self):
        search = input("Enter search book based on (ISBN/Name?Author): ").lower()
        if search == "isbn":
            isbn = input("Enter isbn: ")
            if isbn in self.invetory.keys():
                print(f"ISBN: {isbn}")
                print(self.invetory[isbn])
            else:
                print(self.invetory.get(isbn, "Book not found."))
        elif search == "name":
            name = input("Enter name of the book to search: ").lower()
            for isbn, details in self.invetory.items():
                if details["Name"] == name:
                    print(f"ISBN: {isbn}")
                    print(self.invetory[isbn])
                else:
                    print(self.invetory.get(isbn, "Book not found."))


while True:
    # Menu:
    print("\n1. Add a book")
    print("2. Search for a book")
    print("3. Check book quantity")
    print("4. Rent a Book")
    print("5. Status of a Book")
    print("6. Display all Books")
    print("7. Exit\n")

    # User choice from input:
    choice = int(input("Enter a choice: "))
    # Adding Books:
    if choice == 1:
        book = Bookstore()
        book.add_items()
    # Searching for Books:
    if choice == 2:
        book.searchBook()
    # Existing:
    elif choice == 7:
        print("Exiting the program...")
        break

    else:
        print("Invalid Choice")
