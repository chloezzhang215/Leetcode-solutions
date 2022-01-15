#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        sum = 0

        while l1 or l2:
            if l1 == None:
                cur.next = l2
                l1 = ListNode(0)
            if l2 == None:
                cur.next = l1
                l2 = ListNode(0)
            
            sum += l1.val+l2.val
            cur.next = ListNode(sum%10)
            sum = sum//10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        if sum != 0:
            cur.next = ListNode(sum)
        return head.next
