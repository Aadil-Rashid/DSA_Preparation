class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            num = nums[i]
            hashMap[num] = i
    
        for i in range(len(nums)):
            num = nums[i]
            sec_num = target - num
            if sec_num in hashMap and i != hashMap[sec_num]:
                output = [i, hashMap[sec_num]]
                return output
        return []
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        