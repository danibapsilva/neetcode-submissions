# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = node = ListNode(0)

        curr = head
        while curr:
            if curr.val != val:
                node.next = ListNode(curr.val)
                node = node.next
            curr = curr.next

        return dummy.next
        