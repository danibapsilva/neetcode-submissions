# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        zigzag = False

        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                left, right = node.left, node.right
                
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            
            if zigzag:
                level.reverse()
            zigzag = not zigzag
            res.append(level)

        return res
        
        