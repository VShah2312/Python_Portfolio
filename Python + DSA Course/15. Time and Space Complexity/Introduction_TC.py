"""
Time Complexity: Its actually the rate of which time taken increases with respect to the input size. 
    Time complexity it not about running code once. 
    Time complexity means rate of increase. (theta)

How to measure it? 
    In terms of Big Oh notation -> o()
"""
# Example 1:
# Complexity 3*n +1 
# Time complexity O(3n+1)
i=1
while i <=5:
    print("Hello")
    i+=1


"""
3 steps to calculate TC:
    1. TC, always the worst case
    2. Avoid constants
    3. Avoid lower values
"""

# 1.
# Complexity: best time-> O(2), avg time-> O(4), worst time -> O(5)
# O(5) is what we will use. 
marks =85
if marks>=90:
    print("A")
elif 80<=marks<90:
    print("B") 
elif 70<=marks<80:
    print("C") 
elif 60<=marks<70:
    print("D")
else: 
    print("Fail") 

# 2. and 3.
# O(15N^5+ 10N^2+7) ~ O(N^5)
# Here we know that + 7 isnt going affect our complexity. 
# So we can ignore it. 
# Here N^5 will dominate the function, so we can ignore N^2. 
# So we can say O(N^5)
    


