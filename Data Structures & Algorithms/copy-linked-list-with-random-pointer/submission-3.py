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
        oldToNew = {}
        
        dummy = newHead = Node(0)
        curr = head
        while curr:
            newHead.next = Node(curr.val)
            oldToNew[curr] = newHead.next
            curr = curr.next
            newHead = newHead.next
        
        curr = head
        newHead = dummy.next
        while curr:
            newHead.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
            newHead = newHead.next

        return dummy.next