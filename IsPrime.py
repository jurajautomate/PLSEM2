def isPrime(n):
    if n < 0:
        return False
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    
    for i in range(2, n):
        result = n % i 
        if (result == 0):
            return False
    
    return True

def printPrimes(n):
    for i in range (1, n + 1):
        print(f"Number {i} is prime: {isPrime(i)}")

printPrimes(100)
