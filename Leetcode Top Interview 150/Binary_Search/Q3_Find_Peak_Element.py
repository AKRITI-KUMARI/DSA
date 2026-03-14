class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(low, high):
            while low < high:
                mid = low + (high - low)//2
                if nums[mid] < nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid
            return low
   
        return binary_search(0, len(nums)-1)
    
