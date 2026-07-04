# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left_bound=float('-inf'), right_bound=float('inf')):
            if not root:
                return True
            if not left_bound < root.val < right_bound:
                return False
                
            left_side = dfs(root.left,left_bound,root.val) 
            right_side = dfs(root.right,root.val,right_bound)

            return left_side and right_side
        
        return dfs(root)