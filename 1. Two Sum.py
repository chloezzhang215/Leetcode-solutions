/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
*/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff not in hmap:
                hmap[j] = i
            else:
                return [hmap[diff],i]
