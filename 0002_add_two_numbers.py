class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode(0)
        trav = total
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            
            if l1:
                l1val = l1.val
                l1 = l1.next
            else:
                l1val = 0
                
            if l2:
                l2val = l2.val
                l2 = l2.next
            else:
                l2val = 0
                
            temp = l1val + l2val + carry
            carry = 0
            
            if temp > 9:
                temp = temp % 10
                carry = 1
            
            NewNode = ListNode(temp)
            
            trav.next = NewNode
            trav = NewNode
                      
        return total.next
