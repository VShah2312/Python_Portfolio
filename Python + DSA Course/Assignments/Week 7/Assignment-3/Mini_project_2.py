"""
Online Bookstore Management System: 
"""

import random


class Bookstore:
    def __init__(self) -> None:
        self.invetory = {}
        self.salesData = []

    def add_items(self):
        isbn = input("Enter ISBN of the book to add: ")
        if isbn not in self.invetory.keys():
            details = {}
            details["Name"] = input("Enter name of the book: ").title()
            details["Author"] = input("Enter name of the author: ").title()
            details["Price $"] = float(input("Enter price of the book: "))
            details["Quantity"] = int(input("Enter quantity of the book: "))
            self.invetory[isbn] = details
            print("Book added successfully!")
        else:
            print("Book already exists.")
            print(self.invetory[isbn])

    def searchBook(self):
        search = input("Enter search book based on (ISBN/Name/Author): ").lower()
        if search == "isbn":
            isbn = input("Enter isbn: ")
            if isbn in self.invetory.keys():
                print(f"ISBN: {isbn}")
                print(self.invetory[isbn])
            else:
                print(self.invetory.get(isbn, "Book not found."))
        elif search == "name":
            name = input("Enter name of the book to search: ").title()
            for isbn, details in self.invetory.items():
                if details["Name"] == name:
                    print(f"ISBN: {isbn}")
                    print(self.invetory[isbn])
                else:
                    print(self.invetory.get(isbn, "Book not found."))
        elif search == "author":
            author = input("Enter author of the book to search: ").title()
            for isbn, details in self.invetory.items():
                if details["Author"] == author:
                    print(f"ISBN: {isbn}")
                    print(self.invetory[isbn])
                else:
                    print(self.invetory.get(isbn, "Book not found."))
        else:
            print("Enter valid parameter to search book")

    def updateQuantity(self, search_isbn: str, new_quantity: int):
        if search_isbn in self.invetory.keys():
            self.invetory[search_isbn]["Quantity"] = new_quantity
            print(self.invetory[search_isbn])
            print("Quantity updated.")
        else:
            print("Book not found with this ISBN")

    def processOrder(self, isbn: str, quantity: int, customer_name: str = ""):
        transcation_number = random.randint(100000, 999999)
        if isbn in self.invetory.keys():
            if self.invetory[isbn]["Quantity"] >= quantity:
                self.invetory[isbn]["Quantity"] -= quantity
                self.salesData.append(
                    {
                        "Transcation Number": transcation_number,
                        "ISBN": isbn,
                        "Quantity": quantity,
                        "Customer Name": customer_name,
                        "Revenue": quantity * self.invetory[isbn]["Price $"],
                    }
                )
                print("Checkout sucessful.")
            else:
                print("Insufficient Quantity")
        else:
            print("Book not found with this ISBN")

    def salesReport(self):
        print("Sales Report: ")
        total_revenue = 0
        total_book_sold = 0
        for transcation in self.salesData:
            total_revenue += transcation["Revenue"]
            total_book_sold += transcation["Quantity"]
        print(f"Total Revenue: {total_revenue}")
        print(f"Total Books Sold: {total_book_sold}")

    def displayInventory(self):
        for key, value in self.invetory.items():
            print(f"ISBN: {key}\nDetials: {value}")

    def displaySalesData(self):
        for sale in self.salesData:
            for key, value in sale:
                print(key, value)


book = Bookstore()
while True:
    # Menu:
    print("\n1. Add a book")
    print("2. Search A Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Generate Sales Report")
    print("6. Display Current Invetory")
    print("7. Display Sales Data")
    print("8. Exit\n")

    # User choice from input:
    choice = int(input("Enter a choice: "))

    # Adding Books:
    if choice == 1:
        book.add_items()

    # Searching for Books:
    elif choice == 2:
        book.searchBook()

    # Check book quantity:
    elif choice == 3:
        search_isbn: str = input("Enter ISBN of the book: ")
        new_quanity: int = int(input("Enter updated quantity: "))
        book.updateQuantity(search_isbn, new_quanity)

    # Processs Order:
    elif choice == 4:
        isbn: str = input("Enter isbn: ")
        quantity: int = int(input("Enter quantity: "))
        customer_name: str = input("Enter customer name: ")
        book.processOrder(isbn, quantity, customer_name)

    # Display sales report:
    elif choice == 5:
        book.salesReport()

    # Display inventory
    elif choice == 6:
        book.displayInventory()

    # Display sales Data:
    elif choice == 7:
        book.displaySalesData()

    # Existing:
    elif choice == 8:
        print("Exiting the program...")
        break

    # Invalid choice:
    else:
        print("Invalid Choice")
