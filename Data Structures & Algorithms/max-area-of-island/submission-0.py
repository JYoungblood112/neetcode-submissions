class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        stack = []
        visited = set()
        count = 0
        maxI = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    count+=1
                    visited.add((row, col))
                    stack.append((row, col))

                    while stack:

                        r, c = stack.pop()

                        directions = [(0,1), (1,0), (-1,0), (0,-1)]

                        for i, j in directions:

                            nr = r+i
                            nc = c+j

                            if nr >= 0 and nr < len(grid) and nc >= 0  and nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                count+=1
                                visited.add((nr, nc))
                                stack.append((nr, nc))
                    if count > maxI:
                        maxI = count
                    count = 0
        return maxI
                                

        