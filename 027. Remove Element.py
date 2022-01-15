class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b = 0, 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b

