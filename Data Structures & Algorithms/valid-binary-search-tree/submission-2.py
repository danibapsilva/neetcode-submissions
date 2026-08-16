# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, low, high = q.popleft()

            left, right = node.left, node.right
            if not (low < node.val < high):
                return False
            
            if left:
                q.append((left, low, node.val))
            
            if right:
                q.append((right, node.val, high))

        return True