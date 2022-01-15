# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
            
        return dummy.next
            
