class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min = 5000
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] < min:
                min = nums[mid]
            elif nums[low] <= nums[mid]:
                if(nums[low] < min):
                    min = nums[low]
                low = mid+1
            else:
                high = mid-1
        return min
  
