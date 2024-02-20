# Logical Operators: (To compare two or more conditions)
# and all conditions needs to be satisfied
# or atleast one conditions needs to be satisfied
# not reverses the result.
a = 20
b = 10
c = 5

print(a > b and b > c)  # Answer true (true and true)
print(a < b or b > c)  # Answer true (true or false)
print(a < b and b > c)  # Answer false (false and true)
print(a < b or b < c)  # Answer false (false or false)
print(not (a > b))  # Answer false (reverse of true)

# Examples:
chemistry = int(input("Enter your chemistry grade: "))
physics = int(input("Enter your physics grade: "))
math = int(input("Enter your math grade: "))
print(physics > 33 and chemistry > 33)
print(physics > 33 or chemistry > 33)
print(not (physics > 33 or chemistry > 33))
print(physics > 33 or not chemistry > 33)
print(physics > 33 and not chemistry > 33)
print(physics > 33 and chemistry > 33 and math > 33)
