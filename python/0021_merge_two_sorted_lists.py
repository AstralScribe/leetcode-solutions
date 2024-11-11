from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        out = head

        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next

            head = head.next

        while list1:
            head.next = ListNode(list1.val)
            list1 = list1.next
            head = head.next

        while list2:
            head.next = ListNode(list2.val)
            list2 = list2.next
            head = head.next

        return out.next


def test_solution():
    s = Solution()

    list1 = None
    list2 = ListNode(1)
    list2.next = ListNode(2)

    result = s.mergeTwoLists(list1, list2)
    out = []

    while result:
        out.append(result.val)
        result = result.next

    assert out == [1, 2]
