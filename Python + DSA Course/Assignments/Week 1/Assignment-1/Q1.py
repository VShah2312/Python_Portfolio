# Question 1:
a = 5
b = 10

print(a > 5 and b >= 10)
# Answer: False and True= False

print(a >= 5 or not b > 10)
# Answer: True and not False = True and True = True

print(not (a > 5 and b > 5))
# Answer: not (False and True)= not (False)= True

print(not (a < 10 or not b < 10))
# Answer: not(True or not False)= not(True or True)= not(True)=False

print(not (not a <= 5 or not b >= 10))
# Answer: not(not True or not True ) = not(False or False)= not(False)= True
