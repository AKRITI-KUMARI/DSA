class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while left < right:
            l = right - left
            b = min(height[left], height[right])
            area = l*b
            ans = max(ans, area)
            if b == height[left]:
                left += 1
            else:
                right -= 1
        return ans
    