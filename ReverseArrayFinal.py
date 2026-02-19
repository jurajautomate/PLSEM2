A  = [1, 2, 3, 4, 5]

def reverse_array(array):

    last_index = len(array) - 1
    new_array = []


    while last_index >= 0:
        new_array.append(array[last_index])
        last_index = last_index - 1

    return new_array

print(reverse_array(A)) 