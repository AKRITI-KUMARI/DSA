"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x, y, length):
            # Check if all values in the subgrid are the same
            first_val = grid[x][y]
            uniform = True
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != first_val:
                        uniform = False
                        break
                if not uniform:
                    break
            
            # If uniform, return leaf node
            if uniform:
                return Node(val=bool(first_val), isLeaf=True)
            
            # Otherwise, divide into quadrants
            half = length // 2
            return Node(
                val=True,  # arbitrary when isLeaf=False
                isLeaf=False,
                topLeft=helper(x, y, half),
                topRight=helper(x, y + half, half),
                bottomLeft=helper(x + half, y, half),
                bottomRight=helper(x + half, y + half, half)
            )
        
        return helper(0, 0, len(grid))
