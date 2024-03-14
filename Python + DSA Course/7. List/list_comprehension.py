"""
List Comprehension: Its not used to manipulate the list but to create the list. 
Moreover its slightly faster. Hence used during optimization. 

my_list = []
for i in range(1, 11):
    my_list.append(i)
print(my_list)

Same thing is what list comprehension does. 
"""

my_list = [i for i in range(1, 11)]
print(my_list)
my_list = [1 for i in range(1, 11)]
print(my_list)
my_list = [i + 5 for i in range(1, 11)]
print(my_list)
my_list = [i % 2 for i in range(1, 11)]
print(my_list)
my_list = [i for i in range(1, 101, 5)]
print(my_list)
my_list = [i for i in range(-10, -1, -1)]
print(my_list)
my_list = [i for i in range(10, -1, -1)]
print(my_list)
my_list = [i % 2 == 0 for i in range(1, 11)]
print(my_list)
