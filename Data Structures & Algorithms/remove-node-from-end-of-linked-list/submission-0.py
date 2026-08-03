# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if nodes[-n] == nodes[0]:
            if len(nodes) == 1:
                return None
            else:
                return nodes[1]
        nodes[-(n + 1)].next = nodes[-(n - 1)] if nodes[-n].next else None

        return head