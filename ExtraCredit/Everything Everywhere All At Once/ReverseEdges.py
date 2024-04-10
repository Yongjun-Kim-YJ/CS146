def reverseEdges(adjList):
    newAdjList = {i: [] for i in range(len(adjList))}
    for i, neighbors in adjList.items():
        for j in neighbors:
            newAdjList[j].append(i)
    return newAdjList