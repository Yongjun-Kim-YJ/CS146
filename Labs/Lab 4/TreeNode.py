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