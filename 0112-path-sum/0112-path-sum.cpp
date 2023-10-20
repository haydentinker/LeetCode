/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root!=nullptr){
            if(root->val==targetSum&&root->right==nullptr&&root->left==nullptr){
                return true;
            }else{
                if(root->left==nullptr&&root->right==nullptr){
                    return false;
                }else{
                    return hasPathSum(root->right,targetSum-root->val)+hasPathSum(root->left,              targetSum-root->val);
                }
            }
        }
        return false;
    }

};