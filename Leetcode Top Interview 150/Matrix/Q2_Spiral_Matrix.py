class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        top,down,left,right = 0,m-1,0,n-1
        while top <= down and left <= right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top += 1
            if top > down:
                break
            for i in range(top,down+1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for j in range(right,left-1,-1):
                ans.append(matrix[down][j])
            down -= 1
            if top > down:
                break
            for i in range(down,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans