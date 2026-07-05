# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n+=1
            if n==k: return cur.val
            cur = cur.right



        #using dfs to solve it recusivly
        # self.res = 0
        # self.count = 0
        # def dfs(root,k):
        #     if not root:
        #         return 0
            
        #     dfs(root.left,k)
        #     self.count+=1
        #     if self.count == k: self.res = root.val
        #     dfs(root.right,k)

        # dfs(root,k)
        # return self.res
        