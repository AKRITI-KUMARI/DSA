# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        head = ListNode()
        temp = head
        while p and q:
            if p.val < q.val:
                temp.next = ListNode(p.val)
                p = p.next
                temp = temp.next
            elif q.val <= p.val:
                temp.next = ListNode(q.val)
                q = q.next
                temp = temp.next
        while p:
            temp.next = ListNode(p.val)
            p = p.next
            temp = temp.next
        while q:
            temp.next = ListNode(q.val)
            q = q.next
            temp = temp.next
        return head.next