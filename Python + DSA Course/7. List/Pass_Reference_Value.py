# Pass by value
def change(a: int):
    a = 1000
    print(a)  # Local Value
    print(id(a))  # Local Value


a = 50  # Global Value
change(a)
print(a)
print(id(a))
# Different id's for global and local variable.


# Pass by reference (works for mutable objects). Here we are passing memory not values.
def display(lst: list):
    print(id(lst))
    lst[0] = (
        100  # Updating list locally. Here we are not changing list, we are changing in the memory of the list.
    )
    print(id(lst))


my_list = [3, 4, 5]
display(my_list)
print(my_list, id(my_list))  # Update in the list visibile in global as well.
# Same id for global and local variable.
