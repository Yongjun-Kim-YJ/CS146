1. Initialization: If the root is null, return an empty list as there are no nodes to process.
2. Queue Setup: Initialize a queue that will store nodes at each level to be processed. The root node is the first node to be enqueued.
3. Level Processing:
   - While the queue is not empty, we initiate a loop to process each level.
   - Determine the number of nodes at the current level (queue size at the start of the level).
   - Create a temporary list to hold the node values for the current level.
4. Node Processing:
   - Dequeue each node at the current level, append its value to the temporary list.
   - If a dequeued node has a left child, enqueue the left child.
   - If a dequeued node has a right child, enqueue the right child.
5. Result Construction: After processing all nodes at the current level, add the temporary list to the result list.
6. Continue to Next Level: Proceed to the next iteration (next level in the tree) until all levels are processed.