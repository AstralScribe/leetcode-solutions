from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(llist):
            curr = llist
            out = None

            while curr is not None:
                temp = curr.next
                curr.next = out
                out = curr
                curr = temp

            return out

        right = slow.next
        slow.next = None

        left = head
        right = reverse(right)

        while left and right:
            t1 = left.next
            t2 = right.next

            left.next = right
            if t1:
                right.next = t1

            left = t1
            right = t2


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        while temp.next is not None:
            tail = temp.next
            if tail.next is None:
                break
            while tail.next.next is not None:
                tail = tail.next
            tail.next.next = temp.next
            temp.next = tail.next
            tail.next = None

            temp = temp.next.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s.reorderList(head)


while head is not None:
    print(head.val)
    head = head.next
