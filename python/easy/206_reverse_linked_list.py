from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second = None
        while head is not None:
            second = ListNode(head.val, second)
            head = head.next
        return second
