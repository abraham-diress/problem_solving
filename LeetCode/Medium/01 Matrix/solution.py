class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        visited = set()
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        q = deque([])

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c, 0))
        
        while q:
            r, c, d = q.popleft()
            ans[r][c] = d

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        
        return ans






        