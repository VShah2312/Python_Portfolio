# Introduction:
"""
i=1
while i<=10: 
    print("Hello World ")

Above is an infinite loop as value of i will always be 1. 
So we need to add counter or increase it by 1 after every print. 
"""

i = 1
while i <= 10:
    print("Hello World!")
    i += 1

# Same output for both.
i = 1
while i <= 10:
    i += 1
    print("Hello World!")

# Example 1: Print 1 to 10 using while loop

i: int = 0
while i < 10:
    i += 1
    print(i, end="")
