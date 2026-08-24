# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k

        def dfs(root):
            nonlocal res, count

            if not root:
                return

            if not count:
                res = root.val
                return
            
            dfs(root.left)
            count -= 1
            if not count:
                res = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return res