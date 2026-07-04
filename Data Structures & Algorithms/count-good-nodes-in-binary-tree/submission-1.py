# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root,current_max):
            if not root:
                return 
            if root.val>=current_max: 
                self.res+=1
                current_max = root.val
            dfs(root.left,current_max)
            dfs(root.right,current_max)
        dfs(root,root.val)
        return self.res
            
        