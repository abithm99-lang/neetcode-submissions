# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def postorder(node):
            if node is None:
                return 
            postorder(node.left)
            postorder(node.right)
            node.left,node.right = node.right,node.left
        postorder(root)
        return root
        