class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        res = []
        visited = set()
        email_to_name = {}

        for account in accounts:
            first_email = account[1]
            name = account[0]

            for email in account[1:]:
                email_to_name[email] = name

            graph.setdefault(first_email, [])

            for email in account[2:]:
                graph.setdefault(email, [])

                graph[first_email].append(email)
                graph[email].append(first_email)
        
        for email in graph:
            if email not in visited:
                component = []
                self.dfs(graph, email, component, visited)
                component.sort()
                name = email_to_name[component[0]]
                res.append([name] + component)
        
        return res

    def dfs(self, graph, email, component, visited):
        visited.add(email)
        component.append(email)

        for neighbor in graph[email]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, component, visited)
