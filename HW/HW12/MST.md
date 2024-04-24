### Kruskal's Algorithm
1. Representing the Graph: Model the problem as a graph where each house is a node. The cost of building a well at each house represents an edge connecting the house to a virtual node (representing the water source). The pipes between houses are edges connecting the respective nodes.
2. Sorting Edges: Create a list of all edges, including both the well costs (as edges to the virtual node) and the pipe connections. Sort this list based on the cost of the edges in non-decreasing order.
3. Union-Find Structure: Initialize a Union-Find data structure to keep track of which houses are connected.
4. Processing Edges: Iterate over the sorted list of edges and for each edge, connect the nodes if they are not already in the same set. If they are connected, ignore the edge to avoid cycles.
5. Calculating the Cost: Each time an edge is added, increment the total cost by the cost of that edge. Once all houses are connected, the total cost represents the minimum cost to supply water to all houses.

### Prim's Algorithm
1. Start at the Virtual Node: Initialize the minimum spanning tree with a virtual node representing the water source.
2. Edge Selection: At each step, select the edge with the lowest cost that connects a node in the tree with a node outside the tree.
3. Update the Tree and Costs: Add the selected edge to the tree and update the total cost.
4. Repeat Until All Nodes are Connected: Continue this process until all houses are connected to the tree.