# https://leetcode.com/problems/linked-list-cycle/description/
# https://neetcode.io/problems/linked-list-cycle-detection?list=blind75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(1) space complexity, O(n) time complexity
# Floyd's tortoise and hare algo
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# O(n) space complexity, O(n) time complexity
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         hash_set = set()
#         while head:
#             if head in hash_set:
#                 return True
#             hash_set.add(head)
#             head = head.next
#         return False