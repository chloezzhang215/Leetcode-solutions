class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):
            cur = -1
            index = nums2.index(nums1[i])
            for j in range(index,len(nums2)):
                if nums2[j]>nums1[i]:
                    cur = nums2[j]
                    break
            res.append(cur)


        return res
