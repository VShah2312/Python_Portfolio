def calSum(n1:int, n2:int)-> int|None: 
    if n1<n2:
        sum=0
        while n1<=n2:
            sum+=n1
        return sum
    return "n1 should be smaller"