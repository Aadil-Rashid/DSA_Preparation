# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

class Solution:
    def __init__(self):
        self.hash_obj = dict()
        self.return_word = ""

    def frequencySort(self, s: str) -> str:
        self.hash_obj = self.build_map_obj(s)
        hash_keys = list(self.hash_obj.keys())
        length_of_keys = len(hash_keys)
        heap_obj, heap_len = self.max_heap_builder(hash_keys)
        self.build_return_word(heap_obj, heap_len)
        return self.return_word
    
    # 4- word build
    def build_return_word(self, heap_obj, heap_len):
        print('self.hash_obj==',self.hash_obj)
        print('heap_obj== ', heap_obj)
        for i in range(1, heap_len):
            alpha = heap_obj[i]
            freq = self.hash_obj.get(alpha)
            piece = alpha * freq
            self.return_word += piece

    # 3- heap pop
    # def heap_pop(arr, heap_size):
    #     if heap_size < 1:
    #         return
    #     max_element = arr[1]
    #     arr[1] = arr[heap_size-1]
    #     arr[heap_size-1] = None
    #     heap_size -= 1
        
    #     max_heapify_algorithm(arr, 1, heap_size)
    
    #     return max_element

    # 2- buid a heap
    def max_heap_builder(self, arr): 
        new_heap = [None]+arr
        arr_len = len(new_heap)
        print(new_heap, arr_len)
        for i in range(arr_len-1, 1, -1):
            parent_index = i // 2
            print(i, parent_index)
            curr_count = self.hash_obj.get(new_heap[i])
            parent_count = self.hash_obj.get(new_heap[parent_index])
           
            if curr_count > parent_count:
                new_heap[i], new_heap[parent_index] = new_heap[parent_index], new_heap[i] 
        return new_heap, arr_len
    
    # 1- it returns hash object.
    def build_map_obj(self, given_word):
        map_obj = dict()
        for word in given_word:
            word_count = map_obj.get(word, 0)
            map_obj[word] = word_count + 1

        return map_obj

obj = Solution()
word =  "tree"
obj.frequencySort(word)
