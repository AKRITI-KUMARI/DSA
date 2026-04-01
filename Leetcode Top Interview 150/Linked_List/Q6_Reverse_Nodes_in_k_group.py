# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                node = curr.next
                curr.next = prev
                prev = curr
                curr = node
            start.next = end
            return prev

        temp = head
        count = 0
        while (temp and count < k):
            count += 1
            temp = temp.next
        if count < k:
            return head
        newHead = reverse(head, temp)
        head.next = self.reverseKGroup(temp,k)
        return newHead
    
  