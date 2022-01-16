class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num*-1)
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        
        return heapq.heappop(heap)*-1
