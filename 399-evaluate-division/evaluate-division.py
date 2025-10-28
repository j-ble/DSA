class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # we need to build a graph where each variable points to its related variables with weight s
        # we must build adjacency list graph with weights
        from collections import defaultdict
        graph = defaultdict(dict)
        # we need to populate graph with equations
        # for equation a/b = k, we store: a->b with weight k, and b->a with weight 1/k
        for i, (a, b) in enumerate(equations):
            # a/b = values[i], so a->b has weight values[i]
            graph[a][b] = values[i]
            # b/a =a 1/values[i], so b->a has weight 1/values[i]
            graph[b][a] = 1 / values[i]
        # we define DFA helper to find a path from start to end
        def dfs(start, end, visited):
            # if start not in graph, variable is undefined
            if start not in graph:
                return -1.0
            # if we reached the end, return 1.0 (multiply identity)
            if start == end:
                return 1.0
            # we mark current node as visted 
            visited.add(start)
            # we explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    # we recursively search from neighbor
                    res = dfs(neighbor, end, visited)
                    # if we found a path, multiply weights
                    if res != -1.0:
                        return weight * res
            # no path found
            return -1.0
        # we process each query
        res = []
        for c, d in queries:
            # if either cariables undefined, return -1.0
            if c not in graph or d not in graph:
                res.append(-1.0)
            else:
                # we perform DFS to find c/d
                res.append(dfs(c, d, set()))
        return res
# Time complexity is O(E + Q * (V + E)) where E is equations, Q is queries, V is variable
# Space complexity is O(E) for graph storage + O(V) for recursion stack