class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        count = 1
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                prev[0] = curr[0]
                prev[1] = min(prev[1], curr[1])
            else:
                count += 1
                prev = curr
        return count