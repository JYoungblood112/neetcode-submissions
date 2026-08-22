class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        stack = []

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == "1":
                    stack.append((row, col))
                    grid[row][col] = "0"
                    count += 1

                    while stack:
                        r, c = stack.pop()

                        directions = [(1,0), (0,1), (-1,0), (0,-1)]

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if (
                                nr >= 0
                                and nr < len(grid)
                                and nc >= 0
                                and nc < len(grid[row])
                                and grid[nr][nc] == "1"
                            ):
                                stack.append((nr, nc))
                                grid[nr][nc] = "0"

        return count