package HW12;
import java.util.Arrays;

public class MinCost {

    private int[] parent;
    private int[] rank;

    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        parent = new int[n + 1];
        rank = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        int[][] edges = new int[pipes.length + n][];

        for (int i = 0; i < wells.length; i++) {
            edges[i] = new int[]{0, i + 1, wells[i]};
        }

        for (int i = 0; i < pipes.length; i++) {
            edges[i + n] = new int[]{pipes[i][0], pipes[i][1], pipes[i][2]};
        }

        Arrays.sort(edges, (a, b) -> a[2] - b[2]);

        int totalCost = 0;
        for (int[] edge : edges) {
            if (union(edge[0], edge[1])) {
                totalCost += edge[2];
            }
        }

        return totalCost;
    }

    private int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
        return false;
    }
}
