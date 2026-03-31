# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        sum = carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                sum = sum%10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            if sum > 9:
                sum = sum%10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            if sum > 9:
                sum = sum%10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            l2 = l2.next
        if carry == 1:
            temp.next = ListNode(carry)
        return head.next