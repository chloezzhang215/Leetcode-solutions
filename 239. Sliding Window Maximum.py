#利用双端队列记录当前滑动窗口的元素索引
#队列最左侧元素记录滑动窗口中最大元素的索引
#遍历数组：
#如果队列最左侧索引已不在滑动窗口范围内，弹出队列最左侧索引
#通过循环确保队列的最左侧索引所对应元素值最大
#新元素入队
#从第一个滑动窗口的末尾索引开始将最大值存储到结果res中

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        for i, num in enumerate(nums):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
