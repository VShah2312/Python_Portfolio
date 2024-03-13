"""
Question 1:Make a list of your own. Print the whole list in reverse using FOR loop
and WHILE loop. 
"""

a = [1, 2, 3, 4, 5]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
print()

# OR

for i in range(1, len(a) + 1):
    print(a[-i], end=" ")
print()

# Using while loop

i = 1
while i <= len(a):
    print(a[-i], end=" ")
    i += 1
print()

my_list = [43, 65, "Elon", "Ambani", False, 55.43]

for i in range(0, len(my_list)):
    print(my_list[i])

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
