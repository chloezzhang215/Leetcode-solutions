# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        pre = head
        cur = head.next

        while cur != None:
            tmp = cur.next
            pre.next = tmp
            cur.next = head
            head = cur
            cur = tmp

        return head
            
