#  Binary Gap
def solution(N):
    binary_string = bin(N)[2:]
    zerocount = 0
    maxi = 0
    in_gap = False

    for digit in binary_string:
        if digit == '1':
            if in_gap:
                maxi = max(maxi, zerocount)
            zerocount = 0
            in_gap = True
        elif in_gap:
            zerocount += 1

    return maxi
print(solution(1041))


# Passing car: 
def solution(A):
    zerocount= 0
    result =0 
    for i in A: 
        if i ==0: 
            zerocount +=1
        else:
            result+= zerocount
    return result

# Missing number: 
def missingNumber(self, nums: List[int]) -> int:
    n= len(nums)
    sum_1= (n*(n+1))//2
    sum_2= sum(nums)
    return int(sum_1- sum_2)

#Tape Equilibrium

def solution(A):
    mini= float('inf')
    # Implement your solution here
    for i in range(1,len(A)):
        s1= sum(A[0:i])
        s2= sum(A[i:])
        mini= min(mini, abs((s2-s1)))
    return mini
        
# Rotation: 
def solution(A, K):
    # Implement your solution here
    def reverse_array(arr, start, end): 
        i= start
        j= end 
        while i<=j:
            arr[i], arr[j]= arr[j], arr[i]
            i+=1
            j-=1
    n= len(A)
    k=K%n
    reverse_array(A, n-k, n-1)
    reverse_array(A, 0, n-k-1)
    reverse_array(A,0, n-1)
    return A

# Odd occurence array: 
def solution(A):
    # Implement your solution here
    my_dict= {}
    for i in A:
        my_dict[i]= my_dict.get(i, 0)+1

    for k,v in my_dict.items():
        if v%2 !=0:
            return k
        
# Frog Jump

def solution(X, Y, D):
    # Implement your solution here
    position= X
    jump= 0
    while position <=Y:
        position += D
        jump+=1
    return jump