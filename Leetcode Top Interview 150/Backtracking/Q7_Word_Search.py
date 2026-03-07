class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            if word[k] != board[i][j]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"
                
            found = backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1) or backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1)
            board[i][j] = temp
            return found



        for i in range(len(board)):
            for j in range(len(board[0])):
                found = backtrack(i, j, 0)
                if found == True:
                    return True
        return False
                
