# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        res = ListNode(0)
        dummy = res
        
        while (l1!=None) or (l2!=None):
            dum1 = l1.val if l1 else 0
            dum2 = l2.val if l2 else 0
            
            carry,value = divmod(dum1+dum2+carry,10)
            
            temp = ListNode(value)
            res.next = temp
            
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
            
            res = res.next
        
        if carry > 0:
            
            temp = ListNode(carry)
            res.next = temp
            res = res.next
        
        return dummy.next
            
            
            
            
            
            