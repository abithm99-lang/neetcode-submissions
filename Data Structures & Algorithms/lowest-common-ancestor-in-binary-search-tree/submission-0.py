# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return False
        if root.val == p.val or root.val == q.val:
            return root
        
        left_res = self.lowestCommonAncestor(root.left,p,q) 
        right_res = self.lowestCommonAncestor(root.right,p,q)

        if left_res and right_res:
            return root
        
        return left_res if left_res else right_res