from typing import Optional


class ListNode:
    def __init__(self, val: int, next: "ListNode" = None):
        self.val = val
        self.next = next


class RecentCounter:
    def __init__(self):
        self.history: Optional[ListNode] = None

    def ping(self, t: int) -> int:
        self.history = ListNode(t, self.history)
        curr = self.history
        n = 1
        while curr and curr.next is not None:
            if curr.next.val >= t - 3000:
                n += 1
            else:
                curr.next = None
            curr = curr.next
        return n
