"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# Using the Enumarate function to get the indices of elements in the array
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()       # Sort the respective indices
        begin, end = 0, len(nums) - 1 
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin +=1
            else:
                end -= 1