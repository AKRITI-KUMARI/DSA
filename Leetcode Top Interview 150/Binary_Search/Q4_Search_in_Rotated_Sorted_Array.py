class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high):
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] == target:
                    return mid
                elif nums[low] <= nums[mid]:  # left is sorted
                    if nums[low] <= target < nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:  # right is sorted
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return -1

        return binary_search(0, len(nums) - 1)
