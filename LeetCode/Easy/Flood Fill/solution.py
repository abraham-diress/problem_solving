class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        q = deque([(sr, sc)])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        image[sr][sc] = color

        while q:
            r, c  = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image
        