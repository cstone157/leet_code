# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy_head = ListNode()
        current = dummy_head

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum = l1_val + l2_val + remainder
            remainder = sum // 10
            nxt_val = sum % 10

            current.next = ListNode(nxt_val)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if remainder:
            current.next = ListNode(remainder)

        return dummy_head.next
