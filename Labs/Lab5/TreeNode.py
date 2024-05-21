class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def isValidBST(self, root):
        inorder_result = []
        self.inorder_traversal(root, inorder_result)

        for i in range(1, len(inorder_result)):
            if inorder_result[i] <= inorder_result[i-1]:
                return False
            
        return True
    
    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)
    
# # Test Case
# node1 = TreeNode(3)
# node2 = TreeNode(1)
# node3 = TreeNode(5)

# node1.left = node2
# node1.right = node3

# tree = TreeNode()

# print(tree.isValidBST(node1))