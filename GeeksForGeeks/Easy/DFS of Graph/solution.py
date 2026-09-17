class Solution:
    def dfs(self, adj):
        def dfsOfGraph(node, visited, res, adj):
            # code here
            visited.add(node)
            res.append(node)
            
            for child in adj[node]:
                if child not in visited:
                    dfsOfGraph(child, visited, res, adj)
    
        res = []
        visited = set()
        
        for node in range(len(adj)):
            if node not in visited:
                dfsOfGraph(node, visited, res, adj)
        
        return res
    
    
        
        
            
        
        
        