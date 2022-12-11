# 1- Max Heapify Algorithm (one based index)

# heap = [None, 1, 8, 6, 3, 4, 2, 5]
# heap_size = len(heap)

def max_heapify_algorithm(heap, i, heap_size):
    # base condition
    if i >= heap_size:
        return
    left_child_index,  = 2 * i   
    right_child_index = (2 * i) + 1  # for this formulla to be always true, Tress for heap must be: 
                                    # a perfect BT or Almost Complete BT ==== Complete BT
    largest = float('inf')
    # check largest in left sub tree 
    if (left_child_index <= heap_size and heap[left_child_index] > heap[i]):
        largest = left_child_index
    else:
        largest = i
    # check largest in right sub tree 
    if (right_child_index <= heap_size and heap[right_child_index] > heap[largest]):
        largest = right_child_index
    # swapping logic
    if (largest != i):
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify_algorithm(heap, largest, heap_size)

# print('    input_array = ', heap)
# max_heapify_algorithm(heap, 1, heap_size)
# print('    max_heap =  ', heap)

# 2- Heap Pop()
# max_heap = [None, 9, 8, 7, 5, 4, 3, 2]
# heap_size = len(max_heap)
def heap_pop(arr, heap_size):
    if heap_size < 1:
        return
    max_element = arr[1]
    arr[1] = arr[heap_size-1]
    arr[heap_size-1] = None
    heap_size -= 1
    
    max_heapify_algorithm(arr, 1, heap_size)
    
    return max_element

# print('    max_heap = ', max_heap)
# max_element = heap_pop(max_heap, heap_size)
# print('    poped_element === ', max_element)
# print('    heap after pop =  ', max_heap)



# 3- Heap Push()    // ------------ Precolate Up Algorithm ----------- //
# max_heap = [None, 20, 9, 8, 7, 6, 5, 4, 3]
# heap_size, insert_value = len(max_heap), 12

def heap_push(heap, value, heap_size):
    heap_size += 1
    heap.append(value)
    i = heap_size - 1
    while (i>0 and heap[i//2] < heap[i]):
        heap[i//2], heap[i] = heap[i], heap[i//2]  #swaping operation
        i = i // 2
# print('    max_heap = ', max_heap)
# print('    insert_value == ', insert_value)
# heap_push(max_heap, insert_value, heap_size)
# print('    heap after push operation', max_heap)




# 4- Insert operation
# # 4i) Increase Key       // --- Precolate Up Algorithm --- //

# max_heap = [None, 9, 8, 7, 6, 5, 4, 3]
# heap_size, insert_value, insert_positon = len(max_heap), 50, 5

def insert_increse_key(heap, i, value, heap_size):
    if i > heap_size - 1:
        return 
    heap[i] = value
    while(i>1 and heap[i//2] < heap[i]):
        heap[i], heap[i//2] =  heap[i//2], heap[i]
        i = i // 2
        
# print('   max_heap = ', max_heap)
# print('   insert_value == ', insert_value)
# print('   insert_positon == ', insert_positon)
# insert_increse_key(max_heap, insert_positon, insert_value, heap_size)
# print('   heap after operation', max_heap)



# # 4ii) Decrease Key // --- Precolate Down Algorithm --- //
# max_heap = [None, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# heap_size = len(max_heap)
# insert_value, insert_positon = 0, 2

def insert_decrease_key(heap, i, value, heap_size):
    if i > heap_size - 1:
        return 
    heap[i] = value
    max_heapify_algorithm(heap, i, heap_size)
    
    
# print('   max_heap = ', max_heap)
# print('   insert_value == ', insert_value)
# print('   insert_positon == ', insert_positon)
# insert_decrease_key(max_heap, insert_positon, insert_value, heap_size)
# print('   heap after operation', max_heap)

