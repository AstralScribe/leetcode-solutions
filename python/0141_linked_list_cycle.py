from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head

        while turtle and hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if turtle is hare:
                return True
        return False
