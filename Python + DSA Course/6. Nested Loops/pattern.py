# i goes from top to bottom so it for number of lines . j goes from left to right
print("* * * * *")
print("* * * * *")
print("* * * * *")
print("* * * * *")
print("* * * * *")

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()
# We dont use print("\n") because that gives two lines. One we mentioned, one from default.
# here j is printing.
""" 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(6 - j, end=" ")
    print()

# Method 2: Better method
for i in range(1, 6):
    for j in range(5, 0, -1):
        print(j, end=" ")
    print()

# Here i is printing.
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

"""
1
1 2 
1 2 3
1 2 3 4 
1 2 3 4 5
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""
1 2 3 4 5
1 2 3 4 
1 2 3
1 2 
1
"""
for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=" ")
    print()

# Method 2:

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""
5 
4 5
3 4 5 
2 3 4 5 
1 2 3 4 5 

1. We need to print j as we have different output for each line not like 1 1 1 etc. 
2. pattern is always ending in 5, means j ends in 5. 
3. beginning of each number is 5 -> 1 so i need to go from 5 to 1. 
4. Keep in mind what is printing is not important iteration should be first focus, then we can print. 
"""
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

1. We are printing i
2. Amount we are priting is increasing means j is increasing. 
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2 
5 4 3 
5 4 
5 
"""
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

# OR

for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()
