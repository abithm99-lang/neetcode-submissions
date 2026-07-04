# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack=deque([root])
        res=[]

        while stack:
            temp=[]
            for i in range(len(stack)):
                node = stack.popleft()
                temp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            res.append(temp)
        return res            
        