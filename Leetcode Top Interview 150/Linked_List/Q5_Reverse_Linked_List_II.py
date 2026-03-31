class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
            
        left_p = head
        prev1 = None
        while left > 1:
            prev1 = left_p
            left_p = left_p.next
            left -= 1

        right_p = head
        next2 = None
        while right > 1:
            right_p = right_p.next
            next2 = right_p.next
            right -= 1

        if prev1 == None:
            head = right_p
        else:
            prev1.next = right_p
        temp1 = next2
        p = left_p
        while p != next2:
            temp2 = p.next
            p.next = temp1
            temp1 = p
            p = temp2
        return head