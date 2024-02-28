def change(a: int):
    a = 1000
    print(a)  # Local Value
    print(id(a))  # Local Value


a = 50  # Global Value
change(a)
print(id(a))


# Pass by reference
def display(lst: list):
    print(id(lst))
    lst[0] = 100
    print(id(lst))


my_list = [3, 4, 5]
display(my_list)
print(my_list)
