class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for i in nums:
            if jumps < 0:
                return False
            elif i > jumps:
                jumps = i
            jumps -= 1
        return True
        