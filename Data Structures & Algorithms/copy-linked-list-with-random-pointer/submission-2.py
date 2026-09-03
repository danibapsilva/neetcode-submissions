"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = node = Node(0)

        mp = {}
        curr = head
        while curr:
            node.next = Node(curr.val)
            mp[curr] = node.next
            node, curr = node.next, curr.next
        
        curr, node = head, dummy.next
        while curr:
            node.random = mp[curr.random] if curr.random else None
            node, curr = node.next, curr.next
        
        return dummy.next
            
            
            