class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1

        k = k % len(nums)
        reverse(0, len(nums) - k - 1)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums) - 1)
