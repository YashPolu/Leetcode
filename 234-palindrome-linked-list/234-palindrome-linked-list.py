# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,node):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow ,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        dummy = self.rev(slow)
        
        while dummy:
            if dummy.val!= head.val:
                return False
            head = head.next
            dummy = dummy.next
        
        return True
        