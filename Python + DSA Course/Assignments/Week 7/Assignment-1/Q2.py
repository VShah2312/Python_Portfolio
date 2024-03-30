"""
Question 2: Design a class called Product with properties like name, price,
category, and quantity. Implement a constructor to initialize these
attributes.
Add methods to calculate the total price after applying a discount, ask
discount percent within that method.
"""


class Product:
    """
    Create an object of Product with various attributes and features.
    """

    def __init__(
        self, name: str = "", price: float = 0, category: str = "", quantity: int = 0
    ) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculates total price of Prodcut after discount."""
        discount: float = float(input("Enter discount in percentage: "))
        discount_decimal: float = discount / 100
        total_price: float = self.price - (self.price * discount_decimal)
        return round(total_price, 2)


product_1 = Product("Apple", 2.99, "Produce", 8)
print(product_1.total_price())
