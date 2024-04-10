def adjacencyListToMatrix(adjList):
    n = len(adjList)
    matrix = [[0]*n for _ in range(n)]
    for i, neighbors in enumerate(adjList):
        for j in neighbors:
            matrix[i][j] = 1
    return matrix