class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0 
        visited = set()

        for city in range(len(isConnected)):
            if city not in visited:
                count += 1
                self.dfs(city, isConnected, visited)
              
        return count
    
    def dfs(self, city, grid, visited):
        visited.add(city)
        
        for neighbor in range(len(grid)):
            if grid[city][neighbor] == 1 and neighbor not in visited:
                self.dfs(neighbor, grid, visited)


        
            
        
        


        