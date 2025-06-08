from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        maxval = 0
        i = 0
        for i in range(len(values) // 2):
            ip = len(values) - 1 - i
            maxval = max(maxval, values[ip] + values[i])
        return maxval
