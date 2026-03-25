class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while(n not in d):
            s = str(n)
            sum = 0
            for i in s:
                sum += int(i)**2
            if sum == 1:
                return True
            else:
                d[n] = 1
                n = sum
        return False