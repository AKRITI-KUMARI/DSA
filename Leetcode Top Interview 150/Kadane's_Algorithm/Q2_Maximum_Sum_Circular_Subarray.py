class Solution:
    def kadane(self, arr):
        ans = -float('inf')
        sum = 0
        for i in arr:
            sum += i
            ans = max(ans, sum)
            if sum < 0:
                sum = 0
        return ans
    

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_normal = self.kadane(nums)
        
        # if all elements in nums were negative
        if max_normal < 0: 
            return max_normal
        
        total_sum = sum(nums)

        negative_nums = [-x for x in nums]
        min_subarray = self.kadane(negative_nums)

        max_circular = total_sum + min_subarray  

        return max(max_normal, max_circular)
    
