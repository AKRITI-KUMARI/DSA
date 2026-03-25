class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()
        if len(arr) == 0:
            return 0
        count = 1
        ans = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]+1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans
  