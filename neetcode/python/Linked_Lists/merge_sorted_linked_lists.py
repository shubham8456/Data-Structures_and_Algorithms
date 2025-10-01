# https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://neetcode.io/problems/merge-two-sorted-linked-lists?list=blind75

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next



# Usage

def print_node(head: ListNode):
  while head:
    print(head.val)
    head = head.next

l1_3 = ListNode(4, None)
l1_2 = ListNode(2, l1_3)
l1_1 = ListNode(1, l1_2)

l2_3 = ListNode(5, None)
l2_2 = ListNode(3, l2_3)
l2_1 = ListNode(1, l2_2)

result = Solution().mergeTwoLists(l1_1, l2_1)
print_node(result)
