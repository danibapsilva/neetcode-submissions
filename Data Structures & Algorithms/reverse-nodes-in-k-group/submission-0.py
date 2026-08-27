# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevGroup = dummy = ListNode(0, head)
        fast = head

        while True:
            slow = prevGroup.next
            for _ in range(k):
                if not fast:
                    return dummy.next
                fast = fast.next
            
            prev, curr = fast, slow
            while curr != fast:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            prevGroup.next = prev
            prevGroup = slow
