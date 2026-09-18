from collections import deque

class Solution:
    def isCycle(self, V, edges):

        adj = {i: [] for i in range(V)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(start):
            q = deque([(start, -1)])
            visited.add(start)

            while q:
                node, parent = q.popleft()

                for neighbor in adj[node]:

                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, node))

                    elif neighbor != parent:
                        return True

            return False

        for i in adj:
            if i not in visited:
                if bfs(i):
                    return True

        return False