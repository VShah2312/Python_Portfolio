# 10 14
# 11 14 8 3 12 14 1 7 4 3
from typing import *


# Brute force Solution:
def countFrequency(n: int, m: int, edges: List[List[int]]):
    hash_dict = {}
    for i in edges:
        hash_dict[i] = edges.count(i)
    print(hash_dict)
    answer = []
    for j in range(1, n + 1):
        if j in hash_dict:
            answer.append(hash_dict[j])
        else:
            answer.append(0)
    return answer


edges = [11, 14, 8, 3, 12, 14, 1, 7, 4, 3]
print(countFrequency(10, 14, edges))


from typing import *


def countFrequency(n: int, m: int, edges: List[List[int]]):
    hash_dict = {}
    for i in range(1, m + 1):
        if i in edges:
            hash_dict[i] = edges.count(i)
        else:
            hash_dict[i] = 0
    keys = list(hash_dict.values())
    return keys[:n]


edges = [1, 3, 1, 9, 2, 7]
print(countFrequency(6, 9, edges))
# Input: ‘n’ = 6 ‘x’ = 9 ‘arr’ = [1, 3, 1, 9, 2, 7]
# Output: [2, 1, 1, 0, 0, 0]


def countFrequency(n: int, m: int, edges: List[List[int]]):
    arr_c = edges.copy()
    for i in range(n + 1):
        if (i + 1) in arr_c:
            edges[i] = arr_c.count(i + 1)
        else:
            edges[i] = 0
        return edges


edges = [1, 3, 1, 9, 2, 7]
print(countFrequency(6, 9, edges))
