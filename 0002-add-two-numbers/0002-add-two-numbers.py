# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        answer = head = ListNode()
        
        carry = 0
        
        while l1 or l2 or carry :
            t1 = 0
            t2 = 0
            
            if l1 :
                t1 = l1.val
                l1 = l1.next
            if l2 :
                t2 = l2.val
                l2 = l2.next
                
            carry, val = divmod(t1 + t2 + carry, 10)
            
            answer.next = ListNode(val)
            answer = answer.next
            
        return head.next
            
            