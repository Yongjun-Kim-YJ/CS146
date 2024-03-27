1. Start at the Root: Begin the search from the root of the BST.
2. Traverse the Tree:
   - If both nodes `p` and `q` are less than the current node's value, then the LCA must be in the left subtree. Hence, move to the left child.
   - If both nodes `p` and `q` are greater than the current node's value, then the LCA must be in the right subtree. Hence, move to the right child.
   - If the nodes are on either side of the current node, or one of them matches the current node's value, we have found the split point and the current node is the LCA.
3. Terminate the Search: The search terminates when the split point is found, where one node is on the left, and the other is on the right, or when we directly hit one of the nodes `p` or `q`.