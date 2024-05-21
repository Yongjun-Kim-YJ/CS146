def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for dest, src in prerequisites:
        graph[src].append(dest)
    
    visited = [False] * numCourses
    recStack = [False] * numCourses

    def dfs(course):
        if recStack[course]:
            return False
        if visited[course]:
            return True
        
        visited[course] = True
        recStack[course] = True

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        
        recStack[course] = False
        return True
    
    for course in range(numCourses):
        if not visited[course]:
            if not dfs(course):
                return False

    return True
