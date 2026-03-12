class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)

        ans = None
        for i in range(k):
            ans = -heapq.heappop(pq)

        return ans
