def adjacencyMatrixToList(matrix):
    adjList = {}
    for i, row in enumerate(matrix):
        adjList[i] = [j for j, val in enumerate(row) if val != 0]
    return adjList