# Answer to any comparision be in BOOL 

a= 20 
b= 10
# print(a>b) # Answer True 
# print(a<b) # Answer False 
# b= 20
# print(a>b) #Answer False 
# print(a>=b) # Answer True 
# print(a==b) # Answer True, = is assignment, == is equality comparision 
# print(a!=b) #Answer False != not equal

# Logical Operator 
# and all conditions needs to be satisfied 
# or atleast one conditions needs to be satisfied 
# not reverses the result. 
c= 5
print(a>b and b>c) # answer true (true and true)
print(a<b or b>c) # answer true (true or false)
print(a<b and b>c) # answer false (false and true)
print(a<b or b<c) # answer false (false or false)
print(not(a>b))