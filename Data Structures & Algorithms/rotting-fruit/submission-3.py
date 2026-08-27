class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()

        visited = set()

        minutes = 0

        gFruit = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    gFruit +=1


        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 2 and (row, col) not in visited:

                    queue.append((row,col))

                    visited.add((row, col))

        while queue and gFruit > 0:
            for i in range(len(queue)):

                r, c = queue.popleft()
                directions = [(-1,0), (1,0), (0, -1), (0, 1)]

                for dr, dc in directions:


                        nr = r+dr
                        nc = c+dc
                        if (nr, nc) in visited:
                            continue

                        if nr >= 0  and nr < len(grid) and nc >= 0 and nc < len(grid[row]) and grid[nr][nc] == 1:
                            visited.add((nr, nc))

                            grid[nr][nc] = 2

                            gFruit-=1

                            queue.append((nr, nc))
            minutes+=1
        if gFruit != 0:
            return -1
        
        return minutes

                                



                        



                        



        