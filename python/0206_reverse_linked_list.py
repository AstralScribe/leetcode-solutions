from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        out = None

        while curr is not None:
            temp = curr.next
            curr.next = out
            out = curr
            curr = temp

        return out


def test_solution():
    s = Solution()

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    result = s.reverseList(head)

    out = []

    while result is not None:
        out.append(result.val)
        result = result.next

    assert out == [3, 2, 1, 0]
