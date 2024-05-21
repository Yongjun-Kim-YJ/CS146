import java.util.ArrayList;
import java.util.List;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) { 
        this.val = val; 
    }
    
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
    
    public boolean isValidBST(TreeNode root) {
        // inorder traversal
        List<Integer> inorder = new ArrayList<>();
        inorderTraversal(root, inorder);
        
        // Check if sorted
        for (int i=1; i<inorder.size(); i++) {
            if (inorder.get(i) <= inorder.get(i-1)) {
                return false;
            }
        }
        
        return true;
    }
    
    private void inorderTraversal(TreeNode node, List<Integer> inorder) {
        if (node == null) return;

        inorderTraversal(node.left, inorder);
        inorder.add(node.val);
        inorderTraversal(node.right, inorder);
    }
}
