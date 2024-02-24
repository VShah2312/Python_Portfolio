# 3. Without Parameters, with return
# 4. With Parameters, with return

"""
Question: What is return and what does it do?
"Return" terminates the entire function.
Return by default is none. 
"""


# Example:
def add(num1: int, num2: int, num3: int):
    print(num1 + num2 + num3)


r = add(1, 2, 3)  # As we dont have return none is saved for r.
print(r)

"""
Here our terminal will show 6, None. Because function is not returning anything, first 6 is a print statments result. 
When we are using add, we are passing data but add is not returning anything as of now.
We are seeing value because we are printing it. Function is returning none.  
'None' is data type.  By default function returns 'None'. 
"""


def add_1(num1: int, num2: int, num3: int):
    return num1 + num2 + num3


r = add_1(1, 2, 3)
print(r)  # -> 6
add_1(5, 2, 3)  # Nothing printed
print(add_1(5, 2, 3))  # -> 10

"""
add(1,2,3) Here function is returing but we cant see it as we are not calling that variable. 
Here our fucntion is return a value and we are saving it in variable r. 
Our add_1(5,2,3) is returning but it wont show anything in terminal as value is not printed anywhere. 
input function returns string. 
"""


def add_2(num1: int, num2: int, num3: int):
    print(num1 + num2 + num3)


print(
    add_2(5, 6, 1)
)  # -> 12 , None  (12 is print, function add_2 return none and then that is printed.)


# Hover over input function we can see function return value of data type is str.


def add_3(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


print(add_3(8, 2, 5))  # -> 15

# Similarly add_3 will return value of data type int. We can observe the same by hoverig over add_3.
"""
Question: When to use return and when to use print in a function? 
Answer: We use return we wanna use that value again somewhere else. We use print if we want to show value in terminal only during a run. 
We can use return value multiple times, print happens only during run of the functions. 
"Return" terminates the entire function.
"""
"""
Example: Make 2 functions 
add() takes 3 integers -> sum 
checkOddEven() takes 1 int -> str
It is smarter to use two functions, incase we want to use only add later or only checkOddEven later. 
"""


def add_4(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


def checkOddEven(num: int) -> str:
    if num % 2 == 0:
        return "Even"  # if condition is met function will return 'Even' else function will not go through if
        # and go through rest of the code and return 'Odd'. Remeber: Return terminates the function.
    return "Odd"


print(checkOddEven(add_4(8, 3, 9)))
# This checkOddEven of value which is returned from add.

"""
Make checkOddEven function int -> bool"""

# Method 1:


def checkOddEven_1(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


print(checkOddEven_1(add_4(8, 3, 9)))

# Method 2:


def checkOddEven_1(num: int) -> bool:
    return num % 2 == 0  # As condition returns bool.


print(checkOddEven_1(6))
