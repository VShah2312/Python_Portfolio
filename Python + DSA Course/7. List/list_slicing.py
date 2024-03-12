# List slicing
my_list = [45, 31, 76, 54, 11, 32, 100]

# Result:
result = my_list[0 : len(my_list)]
result = my_list[0::]
result = my_list[0:]
# returns whole list
print(result)

# Steps:
result_2 = my_list[0:6:2]
print(result_2)
# All elements:
result_3 = my_list[:]
print(result_3)
# starts from 0 all the way to end with step 5
result_4 = my_list[::5]
print(result_4)
result_5 = my_list[::10]
print(result_5)
# Default step is +ve 1 so it goes left to right
result_6 = my_list[-4:-1]
print(result_6)
# As for loop wont run, so we will get empty list.
result_6 = my_list[-1:-4]
print(result_6)
# For reversing list
result_7 = my_list[::-1]
print(result_7)
# Example: Gues the results
result_8 = my_list[-2:-4:-2]
print(result_8)
result_8 = my_list[-2:-4:2]
print(result_8)
result_8 = my_list[-5::2]
print(result_8)
result_8 = my_list[-5::-2]
print(result_8)
