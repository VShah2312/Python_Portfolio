"""
Question 3: Make your own list of numbers. Ask a start and end position from User.
Make another different list which will contain number from start to end
position. Use slicing logic. (Same as previous question), but now print the
result in reverse:
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
start: int = int(input("Enter a start number: "))
end: int = int(input("Enter a end number: "))
step: int = int(input("Enter a step: "))
result = [my_list[i] for i in range(end, start - 1, -step)]
print(result)
