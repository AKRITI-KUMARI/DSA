class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        if len(nums) == 0:
            return [-1, -1]

        idx = binary_search(0, len(nums) - 1)
        if idx == -1:
            return [-1, -1]

        ans = []
        i = idx
        while i >= 0:
            if nums[i] != target:
                break
            i -= 1
        ans.append(i + 1)
        i = idx
        while i < len(nums):
            if nums[i] != target:
                break
            i += 1
        ans.append(i - 1)
        return ans
