# 1 to 10

for i in range(1, 11):  # 1 inclusive, 11 excluded.
    print(i, end=" ")

# 5 to 18
for i in range(5, 19):  # 5 inclusive, 19 excluded.
    print(i, end=" ")

start = int(input("Enter Start number: "))
end = int(input("Enter End number: "))

for i in range(start, end + 1):  # 5 inclusive, 19 excluded.
    print(i, end=" ")

# Sum from n1 to n2
start = int(input("Enter Start number: "))
end = int(input("Enter End number: "))
sum = 0
for i in range(start, end + 1):  # 5 inclusive, 19 excluded
    sum = sum + i
    print(sum)

# Step: 2
start = int(input("Enter Start number: "))
end = int(input("Enter End number: "))

for i in range(start, end + 1, 2):
    print(i, end=" ")

# Step: -1
start = int(input("Enter Start number: "))
end = int(input("Enter End number: "))

for i in range(start, end - 1, -1):
    print(i, end=" ")

# if start is bigger then end step needs to be specify step -1.

# Step: 5
start = int(input("Enter Start number: "))
end = int(input("Enter End number: "))

for i in range(start, end + 1, 15):
    print(i, end=" ")

# 10 to -10

for i in range(10, -11, -1):
    print(i, end=" ")
