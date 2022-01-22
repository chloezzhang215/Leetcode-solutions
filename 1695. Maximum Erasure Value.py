class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        max_sum, total = 0, 0
        hmap = {}

        start = 0
        for end in range(len(nums)):
            hmap[nums[end]] = hmap.get(nums[end],0) + 1
            total += nums[end]
            if end - start + 1 == len(hmap):
                max_sum = max(max_sum, total)
            
            while end - start + 1 > len(hmap):
                hmap[nums[start]] -= 1
                if hmap[nums[start]] == 0:
                    del (hmap[nums[start]])
                total -= nums[start]
                start += 1
        
        return max_sum
