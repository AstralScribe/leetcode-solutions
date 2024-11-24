from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trav = head
        trail = ListNode(0, head)
        tail = trail

        while n > 0:
            trav = trav.next
            n -= 1

        while trav:
            trav = trav.next
            tail = tail.next

        tail.next = tail.next.next

        return trail.next
