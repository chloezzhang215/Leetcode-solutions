#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newIndex1 = min(index1 + k//2 - 1, m - 1)
                newIndex2 = min(index2 + k//2 - 1, n - 1)
                pivot1 = nums1[newIndex1]
                pivot2 = nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
            
        m = len(nums1)
        n = len(nums2)
        totalLength = m + n
        if totalLength % 2:
            return getKthElement(totalLength//2+1)
        else:
            return (getKthElement(totalLength//2) + getKthElement(totalLength//2+1)) / 2
