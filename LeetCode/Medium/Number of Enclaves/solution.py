class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        visited = set()

        def dfs(r, c):
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs(nr, nc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
                    if grid[r][c] == 1:
                        dfs(r, c)
        
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    cnt += 1
        
        return cnt


        