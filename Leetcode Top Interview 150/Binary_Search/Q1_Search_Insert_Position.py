class Solution:
    def binary_search(self, nums, low, high, target):
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
  