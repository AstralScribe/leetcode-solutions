from typing import Optional
import dis

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode()
        trav = total
        carry= 0

        while l1 or l2 or carry:
            l1val, l1 = (l1.val, l1.next) if l1 else (0, None)
            l2val, l2 = (l2.val, l2.next) if l2 else (0, None)
                
            temp = l1val + l2val + carry
            val = temp % 10
            carry = temp // 10
            trav.next = ListNode(val)
            trav = trav.next

        return total.next

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode()
        trav = total
        carry= 0

        while l1 and l2:
            l1val, l1 = l1.val, l1.next
            l2val, l2 = l2.val, l2.next
                
            temp = l1val + l2val + carry
            val = temp % 10
            carry = temp // 10
            trav.next = ListNode(val)
            trav = trav.next

        while l1:
            l1val, l1 = l1.val, l1.next
            temp = l1val + carry
            val = temp % 10
            carry = temp // 10
            trav.next = ListNode(val)
            trav = trav.next

        while l2:
            l2val, l2 = l2.val, l2.next
            temp = l2val + carry
            val = temp % 10
            carry = temp // 10
            trav.next = ListNode(val)
            trav = trav.next

        if carry:
            trav.next = ListNode(1)
            trav = trav.next


        return total.next


s = Solution()
dis.dis(s.addTwoNumbers)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

output = s.addTwoNumbers(l1, l2)
while output:
    print(output.val, end="")
    output = output.next

