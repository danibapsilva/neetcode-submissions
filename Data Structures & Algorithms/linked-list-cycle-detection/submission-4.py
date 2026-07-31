# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head.next if head else head
        while f and f.next:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        
        return False