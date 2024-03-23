"""
Print below result: 

World Hello
Shah Vrunda is name My
python doing are We
"""

f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    result = []
    result = line.split()
    result_2 = result[::-1]
    print(" ".join(result_2))
