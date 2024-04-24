from typing import List

class MinCost:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU != rootV:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1
                return True
            return False

        # Start with the cost of wells and add them as edges from a virtual node 0
        edges = [(cost, 0, i + 1) for i, cost in enumerate(wells)]
        # Add the pipes as edges between houses
        edges.extend((cost, house1, house2) for house1, house2, cost in pipes)
        # Sort the edges by cost
        edges.sort()

        total_cost = 0
        # Go through the sorted edges and join the sets
        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost

        return total_cost