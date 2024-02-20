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
