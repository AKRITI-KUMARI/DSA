class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        total = m*n
        low, high = 0, total-1

        while low <= high:
            mid = low + (high - low)//2
            mrow = mid // n
            mcol = mid % n
            if matrix[mrow][mcol] == target:
                return True
            elif matrix[mrow][mcol] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False