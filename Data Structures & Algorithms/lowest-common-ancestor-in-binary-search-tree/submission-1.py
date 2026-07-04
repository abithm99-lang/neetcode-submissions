# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur 


        # finding the p and q in a Binary Tree but this is a Binary search Tree so we can use the BS here
        # if not root:
        #     return False
        # if root.val == p.val or root.val == q.val:
        #     return root
        
        # left_res = self.lowestCommonAncestor(root.left,p,q) 
        # right_res = self.lowestCommonAncestor(root.right,p,q)

        # if left_res and right_res:
        #     return root
        
        # return left_res if left_res else right_res