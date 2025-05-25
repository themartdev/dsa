from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next

        while fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
        return False

