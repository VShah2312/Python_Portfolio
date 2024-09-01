""" """
# Bruteforce: 
def majorityElement(v: list[int]) -> int:
    n= len(v)
    for i in range(len(v)):
        count=0
        for j in range(len(v)):
            if v[j]== v[i]:
                count +=1
            if count >n//2:
                return v[i]

# TC: O(N^2)
# SC: O(1)

# Better: 

def majorityElement(v: list[int]) -> int:
    # Write your code here
    
    hash_map= {}
    for i in range(len(v)):
        hash_map[v[i]]= hash_map.get(v[i],0)+1
    maxi= float("-inf")

    for k,v in hash_map.items():
        if v> maxi: 
            key= k
            maxi= v
    return key

# TC: O(3N/2) -> O(N)
# SC: O(N/2) -> O(N)