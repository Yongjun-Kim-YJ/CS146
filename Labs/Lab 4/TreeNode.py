class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def invertTree(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        return root

# # Test Case
# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)

# print(tree.val)
# print(tree.left.val)
# print(tree.right.val)
# print(tree.left.left.val)
# print(tree.left.right.val)

# tree.invertTree(tree)

# print()
# print(tree.val)
# print(tree.left.val)
# print(tree.right.val)
# print(tree.right.left.val)
# print(tree.right.right.val)