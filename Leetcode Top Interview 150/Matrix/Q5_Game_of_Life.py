class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        if m == 1 and n == 1:
            board[0][0] = 0

        elif m == 1:
            board2 = []
            temp = []
            for j in range(n):
                temp.append(board[0][j])
            board2.append(temp)

            for j in range(n):
                liveNeighbors = 0
                if j != 0 and j != n-1:
                    if board[0][j-1] == 1:
                        liveNeighbors += 1
                    if board[0][j+1] == 1:
                        liveNeighbors += 1
                if board[0][j] == 1 and liveNeighbors < 2:
                    board2[0][j] = 0
                elif board[0][j] == 1 and liveNeighbors == 2:
                    board2[0][j] = 1

            for j in range(n):
                board[0][j] = board2[0][j]                

        
        elif n == 1:
            board2 = []
            for i in range(m):
                temp = []
                temp.append(board[i][0])
                board2.append(temp)

            for i in range(m):
                liveNeighbors = 0
                if i != 0 and i != m-1:
                    if board[i-1][0] == 1:
                        liveNeighbors += 1
                    if board[i+1][0] == 1:
                        liveNeighbors += 1
                if board[i][0] == 1 and liveNeighbors < 2:
                    board2[i][0] = 0
                elif board[i][0] == 1 and liveNeighbors == 2:
                    board2[i][0] = 1

            for i in range(m):
                board[i][0] = board2[i][0]                


        else:
            board2 = []
            for i in range(m):
                temp = []
                for j in range(n):
                    temp.append(board[i][j])
                board2.append(temp)

            
            for i in range(m):
                for j in range(n):
                    liveNeighbors = 0
                    if i == 0 and j == 0:
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                    elif i == 0 and j == n-1:
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                    elif i == m-1 and j == n-1:
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                    elif i == m-1 and j == 0:
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                    elif i == 0 and (j != 0 and j != n-1):
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                        if board[i+1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                    elif i == m-1 and (j != 0 and j != n-1):
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                        if board[i-1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                    elif j == 0 and (i != 0 and i != m-1):
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                    elif j == n-1 and (i != 0 and i != m-1):
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                    else:
                        if board[i-1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i-1][j] == 1:
                            liveNeighbors += 1
                        if board[i-1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j+1] == 1:
                            liveNeighbors += 1
                        if board[i+1][j] == 1:
                            liveNeighbors += 1
                        if board[i+1][j-1] == 1:
                            liveNeighbors += 1
                        if board[i][j-1] == 1:
                            liveNeighbors += 1
                        

                    if board[i][j] == 1 and liveNeighbors < 2:
                        board2[i][j] = 0
                    elif board[i][j] == 1 and (liveNeighbors == 2 or liveNeighbors == 3):
                        board2[i][j] == 1
                    elif board[i][j] == 1 and liveNeighbors > 3:
                        board2[i][j] = 0
                    elif board[i][j] == 0 and liveNeighbors == 3:
                        board2[i][j] = 1


            for i in range(m):
                for j in range(n):
                    if board2[i][j] == 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1