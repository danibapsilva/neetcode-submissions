# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, stack = head, []
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        
        dummy = node = ListNode()
        for num in stack:
            node.next = ListNode(num)
            node = node.next
        return dummy.next