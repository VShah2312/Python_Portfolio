"""
Question 1: Make your own list of numbers. Ask a start and end position from User.
Print the list from start position to end position using without using Slicing.
"""

my_list = [45, 31, 76, 54, 11, 32, 100]

start: int = int(input("Enter a start number: "))
end: int = int(input("Enter a end number: "))
step: int = int(input("Enter a step: "))
for i in range(start, end + 1, step):
    print(my_list[i], end=" ")
