class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if len(board) == 0:
            return 
        
        if len(board) == 1:

            return

        stack = []

        visited = set()

        for row in range(len(board)):
            for col in range(len(board[row])):

                if (row, col) in visited:
                    continue

                if (row == 0 or row == len(board) - 1 or col == 0 or col == len(board[row])-1) and board[row][col] == "O":

                    stack.append((row, col))

                    visited.add((row, col))

                    board[row][col] = "E"


                    while stack:

                        r, c = stack.pop()

                        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

                        for dr, dc in directions:

                            nr = r+dr
                            nc = c+dc

                            if (nr, nc) in visited:
                                continue

                            if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[row]) and board[nr][nc] == "O":

                                board[nr][nc] = "E"

                                visited.add((nr, nc))

                                stack.append((nr, nc))
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == "E":
                    board[row][col] = "O"

        
        return
                        





        