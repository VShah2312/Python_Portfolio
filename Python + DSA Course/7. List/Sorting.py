my_list = [["Anirudh", 76], ["Vandana", 26], ["Akul", 67], ["Sanjay", 92]]
print(my_list[0][1])
print(my_list[2][1])
print(my_list[3][-1])
print(my_list[-4][-1])

my_list.sort()  # This sorts by ASCI value. Sort is only available for List. Changes the list.
print(my_list)
# It sorted by ASCI value of 0 elements of list with in the list. Names here

my_list_2 = [[76, "Anirudh"], [26, "Vandana"], [67, "Akul"], [92, "Sanjay"]]
my_list_2.sort()
print(my_list_2)  # Here it will be sorted by age, as they are the first element.
# Sort exists only in list.


x = sorted(my_list)
# This returns and doesnt change in the list. Sorted is available for all data type (Dict etc)
print(x)

# How to filter using a specific position:
# So instead of changing the list like in line 11, we can sort using a key.
my_list.sort(key=lambda x: x[1], reverse=True)
print(my_list)


x = sorted(my_list, key=lambda x: x[1])
print(x)
