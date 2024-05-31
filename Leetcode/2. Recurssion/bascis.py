# count = 1


# def func():
#     global count
#     print(count)
#     if count == 5:
#         return
#     count += 1
#     func()


# func()
from typing import List

result = []


def printNos(x: int, i=1) -> List[int]:
    global result
    # Write your code here
    if i > x:
        return result
    result.append(i)
    i += 1
    printNos(x, i)


print(printNos(5))
