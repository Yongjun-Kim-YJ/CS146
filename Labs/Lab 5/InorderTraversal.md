1. Perform Inorder Traversal: Start by performing an inorder traversal of the binary tree. In inorder traversal, we visit nodes in the order: left, root, right.
2. Check for Sorted Sequence: During the inorder traversal, store the values of the nodes in a list. Since the nodes are visited in sorted order in a valid BST, the list should be sorted in ascending order if the tree is a valid BST.
3. Check for Sortedness: After the traversal, iterate through the list of values and check if they are sorted in ascending order.
4. Return Result: If the values are sorted, return true, indicating that the tree is a valid BST. Otherwise, return false.
