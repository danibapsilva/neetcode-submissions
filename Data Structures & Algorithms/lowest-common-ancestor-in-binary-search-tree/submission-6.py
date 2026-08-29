# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        while lca:
            if max(p.val, q.val) < lca.val:
                lca = lca.left
            elif min(p.val, q.val) > lca.val:
                lca = lca.right
            else:
                return lca