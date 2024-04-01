"""
Library Management System
"""


class Books:
    def __init__(self) -> None:
        self.isbn: str = input("Enter ISBN: ")
        self.name: str = input("Enter name of the book: ").title()
        self.price: float = float(input("Enter price: "))
        self.quantity: int = int(input("Enter quantity: "))
        self.is_rented: bool = False
        # self.status:str= "Available"

    def displayAllInfo(self) -> None:
        print(f"ISBN: {self.isbn}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        # print(f"Status: {self.status}")

    def checkQuantity(self) -> int:
        return self.quantity

    def rentBook(self) -> bool:
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def statusBook(self) -> str:
        if self.quantity > 0:
            return "Book is available for rent."
        return "Book is unavialble at this time."


# Accounts is list of objects from Bank Class
library: list[Books] = []

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
        x = Books()
        library.append(x)
        print("Book added successfully!")

    # Search for a book:
    elif choice == 2:
        search_isbn = input("Enter ISBN to search: ")
        exists = False
        for book in library:
            if book.isbn == search_isbn:
                print("Book found: ")
                book.displayAllInfo()
                exists = True
        if not exists:
            print("Book not found.")

    # Check book quantity:
    elif choice == 3:
        check_quantity = input("Enter ISBN to check quantity: ")
        exists = False
        for book in library:
            if book.isbn == check_quantity:
                print("Quantity Available: ", book.checkQuantity())
                exists = True
        if not exists:
            print("Book not found.")

    # Rent a book:
    elif choice == 4:
        rent_book = input("Enter ISBN to rent: ")
        exists = False
        for book in library:
            if book.isbn == rent_book:
                exists = True
                if book.rentBook() == True:
                    print("Book rented sucessfully.")
                else:
                    print("Book unavailable at this time.")
        if not exists:
            print("Book not found.")

    # Status of a book:
    elif choice == 5:
        status_book = input("Enter ISBN of book for status: ")
        exists = False
        for book in library:
            exists = True
            if book.isbn == status_book:
                print(book.statusBook())
        if not exists:
            print("Book not found.")

    # Display all books:
    elif choice == 6:
        for book in library:
            book.displayAllInfo()

    # Existing:
    elif choice == 7:
        print("Exiting the program...")
        break

    else:
        print("Invalid Choice")
