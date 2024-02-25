# BREAK, CONTINUE
"""
BREAK: It leaves the loop and everything after is skipped. While loops stops when condition is met. 
BREAK stops the loop on provided conditions. 
CONTINUE: its skips everything written after tht and it goes to the next iteration. 
PASS: does nothing. Literally. It skips that line, go to next line. 
"""
i = 1
while i <= 10:
    print(i, end=" ")
    if i == 5:
        break  # Get out of the loop.
    i += 1
print()

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
    if i == 5:
        break  # Get out of the loop.
print()


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # it will skipp everything after it.
    print(i, end=" ")

print("Done")

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     if i == 5:
#         continue  # it will skipp everything after it. so value of i will not increase, thus it is stuck in infinite loop.
#     i += 1
# print("Done") # This will not print as loop doesnt close ever.

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
    if i == 5:
        continue  # it will skipp everything after it.

print("Done")
pass
print("Hello")
