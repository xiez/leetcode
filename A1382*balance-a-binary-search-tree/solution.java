/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void inorder(TreeNode node, ArrayList lst) {
        if (node == null) {
            return;
        }
        inorder(node.left, lst);
        lst.add(node.val);
        inorder(node.right, lst);
    }

    public TreeNode _lstToBST(ArrayList<Integer> lst, int low, int high) {
        if (low > high) {
            return null;
        }
        
        int mid = (low + high) / 2;
        //System.out.println(lst.get(mid));
        TreeNode root = new TreeNode(lst.get(mid));
        root.left = _lstToBST(lst, low, mid - 1);
        root.right = _lstToBST(lst, mid + 1, high);
        return root;    
    }
    
    public TreeNode orderedListToBalanceBST(ArrayList<Integer> lst) {
        int low = 0;
        int high = lst.size() - 1;
        int mid = (low + high) / 2;
        
        TreeNode root = new TreeNode(lst.get(mid));
        root.left = _lstToBST(lst, low, mid - 1);
        root.right = _lstToBST(lst, mid + 1, high);
        return root;
    }
    
    public TreeNode balanceBST(TreeNode root) {
        ArrayList<Integer> lst = new ArrayList<Integer>();
        inorder(root, lst);
        
        TreeNode ret = orderedListToBalanceBST(lst);
        return ret;
    }
}
