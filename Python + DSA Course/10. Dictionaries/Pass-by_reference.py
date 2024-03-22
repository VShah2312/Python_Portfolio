# Pass by reference: Mutuable

from typing import Dict

# Dict[str, int] -> keys :str, value: int


def greet(dict: Dict[str, int]) -> None:
    k = input("Enter key: ")
    v = int(input("Enter value: "))
    dict[k] = v


my_dict = {"vrunda": 75, "akul": 89, "muskan": 52, "akul": 34}

print(my_dict)  # Original dict has been printed
greet(my_dict)  # dict in updated in greet
print(
    my_dict
)  # we will see dict will be updated here as well. As its passing by reference.
