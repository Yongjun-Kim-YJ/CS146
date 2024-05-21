package Labs.Lab4;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public TreeNode invertTree(TreeNode root) {
        if(root == null){
            return null;
        }

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }

    // public static void main(String[] args) {
    //     TreeNode tree = new TreeNode(1);
    //     tree.left = new TreeNode(2);
    //     tree.right = new TreeNode(3);
    //     tree.left.left = new TreeNode(4);
    //     tree.left.right = new TreeNode(5);

    //     System.out.println(tree.val);
    //     System.out.println(tree.left.val);
    //     System.out.println(tree.right.val);
    //     System.out.println(tree.left.left.val);
    //     System.out.println(tree.left.right.val);

    //     tree.invertTree(tree);

    //     System.out.println(tree.val);
    //     System.out.println(tree.left.val);
    //     System.out.println(tree.right.val);
    //     System.out.println(tree.right.left.val);
    //     System.out.println(tree.right.right.val);
    // }
}