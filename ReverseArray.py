A  = [1, 2, 3, 4, 5]

def reverse_array(array, low, high):
    if (low >= high):
        return
    temp = array[high]
    array[high] = array[low]
    array[low] = temp
    reverse_array(array, low + 1, high - 1)

reverse_array(A, 0, len(A) - 1)
