#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,res = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(count,res)
                count = 0
                
        res = max(count,res)
        return res
