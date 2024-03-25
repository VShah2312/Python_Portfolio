"""
Print below result: 

World Hello
Shah Vrunda is name My
python doing are We
"""

f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    result = line.split()
    print(result)
    result_2 = result[::-1]
    print(result_2)
    print(" ".join(result_2))
f.close()


"""
Print below results: 
dlroW olleH
adnurV si sihT
doog si nohtyP
"""
f = open("hello.txt", "r")

for line in f:
    result = line.strip()
    print(result[::-1])
