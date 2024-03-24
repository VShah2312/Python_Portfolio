"""
Question 3: Write a Python dictionary that stores information about different
fruits. Write a program that asks the user to input a fruit name and then
prints its color. Handle the KeyError exception if the input fruit name is not
found in the dictionary.
"""


def fruitColor(my_dict: dict):
    try:
        fruit = input("Enter a fruit name: ").lower()
        return my_dict[fruit]
    except KeyError:
        return "Fruit name not found in the dictionary."
    except:
        return "Some unknown error has occured."


my_dict = {"orange": "orange", "banana": "yellow", "pear": "green", "apple": "red"}
print(fruitColor(my_dict))

# Solution:
fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple",
    "watermelon": "green",
    "pineapple": "yellow",
}


def getColor(fruit_name: str):
    try:
        color = fruits[fruit_name]
        print(f"The color of {fruit} is {color}.")
    except KeyError:
        print("Fruit not found in the dictionary.")


fruit = input("Enter a fruit name = ").lower()
getColor(fruit)
