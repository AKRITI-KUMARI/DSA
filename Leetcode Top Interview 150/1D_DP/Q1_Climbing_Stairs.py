class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a=1
        b=2
        for i in range(n-2):
            t = b
            b = a+b
            a = t
        return b
    