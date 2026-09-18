class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        edge = ([[0, c] for c in range(len(board[0]))] + 
        [[r, 0] for r in range(len(board))] +
        [[len(board) - 1, c] for c in range(len(board[0]))] +
        [[r, len(board[0]) - 1] for r in range(len(board))])

        q = deque([])

        def bfs(r, c):
            q.append([r, c])

            while q:
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in visited and board[nr][nc] == "O":
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))

                        
        for cell in edge:
            r, c = cell

            if (r, c) not in visited and board[r][c] == "O":
                visited.add((r, c))
                bfs(r, c)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited and board[row][col] == "O":
                    board[row][col] = "X"
        


        