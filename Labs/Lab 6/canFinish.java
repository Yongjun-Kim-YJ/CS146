import java.util.ArrayList;

public class canFinish {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        for (int i=0;i<numCourses;i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prerequisiteCourse = prerequisite[1];
            graph[prerequisiteCourse].add(course);
        }
        
        boolean[] visited = new boolean[numCourses];
        boolean[] recStack = new boolean[numCourses];
        
        class GraphCycleDetector {
            public boolean isCyclic(int course) {
                if (recStack[course]) {
                    return true;
                }
                if (visited[course]) {
                    return false;
                }
                
                visited[course] = true;
                recStack[course] = true;
                
                for (Integer neighbor : graph[course]) {
                    if (isCyclic(neighbor)) {
                        return true;
                    }
                }
                
                recStack[course] = false;
                return false;
            }
        }
        
        GraphCycleDetector g = new GraphCycleDetector();

        for (int i=0;i<numCourses;i++) {
            if (!visited[i]) { 
                if (g.isCyclic(i)) {
                    return false;
                }
            }
        }
        
        return true;
    }
}
