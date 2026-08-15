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
            if p.val > lca.val and q.val > lca.val:
                lca = lca.right
            elif p.val < lca.val and q.val < lca.val:
                lca = lca.left
            else:
                return lca