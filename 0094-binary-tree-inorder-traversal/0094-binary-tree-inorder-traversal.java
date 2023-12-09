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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        ArrayList<Integer> result = new ArrayList<Integer>();
        ArrayList<TreeNode> stack = new ArrayList<TreeNode>();
        TreeNode curr=root;
        while(curr!=null||stack.size()!=0){
            while(curr!=null){
                stack.add(curr);
                curr=curr.left;
            }
            curr=stack.remove(stack.size()-1);
            result.add(curr.val);
            curr=curr.right;
        }
        return result;
        }
}