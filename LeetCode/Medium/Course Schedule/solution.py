class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visited = set()
        path = set()

        def detect(node):
            visited.add(node)
            path.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    if detect(neighbor): 
                        return True
                elif neighbor in path:
                    return True
            
            path.remove(node)
            return False

        for u, v in prerequisites:
            adj[v].append(u)
        
        for i in range(numCourses):
            if i not in visited:
                if detect(i):
                    return False
        
        return True 
      