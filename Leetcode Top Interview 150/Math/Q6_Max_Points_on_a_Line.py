from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        ans = 0
        for i in range(n):
            slopeCount = defaultdict(int)
            samePoints = 1
            maxSlope = 0
            x1, y1 = points[i]
            
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                
                if dx == 0 and dy == 0:
                    samePoints += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1 
                
                slopeCount[(dx, dy)] += 1
                maxSlope = max(maxSlope, slopeCount[(dx, dy)])
            
            ans = max(ans, samePoints + maxSlope)
        
        return ans