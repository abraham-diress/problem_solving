class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    self.mark_island(r, c, grid)
        
        return count 
    
    def mark_island(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 
        if grid[row][col] != '1':
            return 
            
        grid[row][col] = '0'
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            self.mark_island(row + dr, col + dc, grid)
        