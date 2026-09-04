class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        def bfs(ocean):
            q = deque(ocean)
            reachable = set(ocean)

            while q:
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and 
                       heights[nr][nc] >= heights[r][c] and 
                        (nr, nc) not in reachable):
                       
                       reachable.add((nr, nc))
                       q.append((nr, nc))
            
            return reachable 
        
        pacific_start = ([(0, c) for c in range(len(heights[0]))] + 
                         [(r, 0) for r in range(len(heights))])
        atlantic_start = ([(len(heights) - 1, c) for c in range(len(heights[0]))] + 
                          [(r, len(heights[0]) - 1) for r in range(len(heights))])

        pacific = bfs(pacific_start)
        atlantic = bfs(atlantic_start)

        return list(pacific & atlantic)
        