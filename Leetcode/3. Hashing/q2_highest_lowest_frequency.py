"""
Question: https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382
"""

from typing import List


def getFrequencies(v: List[int]):
    answer = []
    hash_map = {}
    for num in v:
        hash_map[num] = hash_map.get(num, 0) + 1

    # TC: creating hash_map -> O(N)
    max_occurence = max(hash_map.values())
    min_occurence = min(hash_map.values())
    max_value = float("inf")
    min_value = float("inf")
    # TC: iterating through hash_map -> O(N)
    for key, value in hash_map.items():
        if value == max_occurence:
            max_value = min(key, max_value)

        if value == min_occurence:
            min_value = min(key, min_value)
    answer.append(max_value)
    answer.append(min_value)
    return answer


print(getFrequencies([10, 10, 10, 3, 3, 3]))


# Solution:

from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    # Write your code here
    n = len(v)
    hashMap = {}
    for num in v:
        if hashMap.__contains__(num):
            hashMap[num] = 1 + hashMap[num]
        else:
            hashMap[num] = 1
    print(hashMap)
    minFreq = float("inf")
    minElement = float("inf")
    maxFreq = float("-inf")
    maxElement = float("inf")

    for key, freq in hashMap.items():
        if freq > maxFreq or freq == maxFreq and key < maxElement:
            maxFreq = freq
            maxElement = key
        if freq < minFreq or freq == minFreq and key < minElement:
            minFreq = freq
            minElement = key

    return [maxElement, minElement]


a = [10, 10, 10, 9, 9, 9]
print(getFrequencies(a))
b = [1, 2, 1, 1, 3, 4]
print(getFrequencies(b))
