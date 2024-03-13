"""
Lambda functions: Anonymus functions. So we will need to save it in a variable (can be name of the function) 
When to you lambda function: When you dont have much logic build up. Only one line statements are allowed. 
"""

# Example:
# def add(a,b):
#     return a+b
add = lambda a, b: a + b
mult = lambda a, b, c: a * b * c
# Lambda and Turnary together
mult = lambda a, b, c: a * b * c if a != 0 and b != 0 and c != 0 else "Invalid"

print(add(1, 5))
print(mult(4, 5, 6))

# Create a lambda function 15-> list[int] -> [1,2,3,..., 15]
# Lambda and List Comprehensions
make_list = lambda num: [i for i in range(1, num + 1)]
print(make_list(15))
