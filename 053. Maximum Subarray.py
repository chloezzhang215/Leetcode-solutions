##分治法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        return self.getMax(nums,0,len(nums)-1)

    def getMax(self,nums,left,right):
        if left == right:
            return nums[left]
        mid = left + (right-left)//2
        leftMax = self.getMax(nums,left,mid)
        rightMax = self.getMax(nums,mid+1,right)
        crossMax = self.getCrossMax(nums,left,mid,right)
        return max(leftMax,rightMax,crossMax)
        
    def getCrossMax(self,nums,left,mid,right):
        leftMax = 0
        leftStart = mid - 1
        s1 = 0
        while leftStart >= left:
            s1 += nums[leftStart]
            leftMax = max(leftMax, s1)
            leftStart -= 1

        rightMax = 0
        rightStart = mid + 1
        s2 = 0
        while rightStart <= right:
            s2 += nums[rightStart]
            rightMax = max(rightMax, s2)
            rightStart += 1
            
        return leftMax + nums[mid] + rightMax
      
##动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        pre = 0
        res = nums[0]
        for i in range(size):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res
