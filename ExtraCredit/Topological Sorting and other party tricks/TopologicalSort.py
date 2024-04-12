from collections import deque

# Kahn's Topological Sort
def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    top_order = []

    while queue:
        u = queue.popleft()
        top_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(top_order) == len(graph):
        return top_order
    else:
        return []

# BFS
def bfs_topological_sort(graph):
    return kahn_topological_sort(graph)

# DFS
def dfs_visit(node, graph, visited, temp_marked, result):
    if temp_marked[node]:
        return False
    if visited[node]:
        return True
    
    visited[node] = temp_marked[node] = True
    for neighbor in graph[node]:
        if not dfs_visit(neighbor, graph, visited, temp_marked, result):
            return False
    temp_marked[node] = False
    result.append(node)
    return True

def dfs_topological_sort(graph):
    visited = {node: False for node in graph}
    temp_marked = {node: False for node in graph}
    result = []

    for node in graph:
        if not visited[node]:
            if not dfs_visit(node, graph, visited, temp_marked, result):
                return []
    return result[::-1]

# Test Case
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F', 'G'],
    'G': ['H'],
    'H': ['F'],
    'F': []
}

print("Kahn's Algorithm Topological Sort:", kahn_topological_sort(graph))
print("BFS Topological Sort:", bfs_topological_sort(graph))
print("DFS Topological Sort:", dfs_topological_sort(graph))
