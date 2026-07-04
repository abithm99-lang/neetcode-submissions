# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        res = []

        while stack:
            temp = []
            # Freeze the queue length for the current level
            for i in range(len(stack)):
                node = stack.popleft()
                
                # Append current node value to the level tracker
                temp.append(node.val)
                
                # FIX 1: Only queue child nodes if they actually exist (are not None)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
            # FIX 2: Use .append() to add the single rightmost integer from this level
            res.append(temp[-1])
            
        return res
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     stack = deque([root])
    #     res = []

    #     while stack:
    #         temp = []
    #         for i in range(len(stack)):
    #             node = stack.popleft()
    #             if node:
    #                 temp.append(node.val)
    #                 stack.append(node.left)
    #                 stack.append(node.right)
    #         if temp: res.append(temp[-1])
    #     return res
        