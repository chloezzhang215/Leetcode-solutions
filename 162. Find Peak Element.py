class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                left = mid + 1
            elif nums[mid]<nums[mid-1]:
                right = mid
        if left == right == len(nums)-1:
            return len(nums)-1
        if left == right == 0:
            return 0
   
