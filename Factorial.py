def factorial(number):
    if number < 0:
        return
    
    accumulator = number
    
    while number > 1:
        accumulator = accumulator * number - 1
        number = number - 1
    
    return accumulator

factorial(4)

def factorial(number):
    if (number <= 1):
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(4))
