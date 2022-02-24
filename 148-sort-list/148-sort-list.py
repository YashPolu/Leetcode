# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid(self,node):
        slow = fast = node
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def merge(self,node1,node2):
        dummy = curr = ListNode()
        intMax = float('inf')
        
        while node1 or node2:
            val1 = node1.val if node1 else intMax
            val2 = node2.val if node2 else intMax
            
            if val1 < val2:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            
            curr= curr.next
        
        return dummy.next
    
    def mergeSort(self,node):
        if not node or not node.next:
            return node
        
        mid = self.mid(node)
        nextNode = mid.next
        mid.next = None
        
        firstNode = self.mergeSort(node)
        secondNode = self.mergeSort(nextNode)
        
        return self.merge(firstNode,secondNode)
  
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
        