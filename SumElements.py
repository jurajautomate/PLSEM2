def sumElementsUpToIncluding(list, n):
    
    result = 0
    
    for i in range(0, n+1):
        result += list[i]
        
    return result
    
print(sumElementsUpToIncluding([1,2,3,4,5],4))