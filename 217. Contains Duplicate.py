class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        hmap = {}

        for num in nums:
            if num not in hmap:
                hmap[num] = hmap.get(num,1)
            else:
                hmap[num] = hmap.get(num)+1 

        for key in hmap.keys():
            if hmap.get(key) > 1:
                return True
                
        return False
