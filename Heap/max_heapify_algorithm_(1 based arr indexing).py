# Max Heapify Algorithm (one based index)

arr = [0, 1, 8, 6, 3, 4, 2, 5]
size = len(arr)

def max_heapify_algorithm(arr, i):
    # stopping condition
    if i >= size:
        return
    
    left_child_index = 2 * i
    right_child_index = (2 * i) + 1
    largest = float('inf')
    
    # check largest left 
    if (left_child_index <= size and arr[left_child_index] > arr[i]):
        largest = left_child_index
    else:
        largest = i
    # right
    if (right_child_index <= size and arr[right_child_index] > arr[largest]):
        largest = right_child_index
    
    # swap 
    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify_algorithm(arr, largest)

print('input_array = ', arr)
max_heapify_algorithm(arr, 1)
print('max_heapify_array =  ', arr)