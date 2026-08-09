# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        carry = 0
        while l1 or l2 or carry:
            added = carry

            if l1:
                added += l1.val
                l1 = l1.next
            
            if l2:
                added += l2.val
                l2 = l2.next
            
            node.val = added % 10
            carry = added // 10 # if two digits

            if l1 or l2 or carry:
                node.next = ListNode()
                node = node.next


        
        # node.next = l1 or l2

        return dummy
