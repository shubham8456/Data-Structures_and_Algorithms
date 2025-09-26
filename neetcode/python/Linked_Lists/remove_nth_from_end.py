# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode250

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        left = start # Starts from dummy node on left to head
        right = head

        while right and n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return start.next
