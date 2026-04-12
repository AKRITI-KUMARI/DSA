# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, a, b):
        dummy = ListNode()
        ptr1, ptr2, ptr3 = a, b, dummy
        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr3.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr3.next = ptr2
                ptr2 = ptr2.next
            ptr3 = ptr3.next
        
        while ptr1:
            ptr3.next = ptr1
            ptr1 = ptr1.next
            ptr3 = ptr3.next
        
        while ptr2:
            ptr3.next = ptr2
            ptr2 = ptr2.next
            ptr3 = ptr3.next
        
        return dummy.next

    def mergeKListsHelper(self, lists, low, high):
        if low == high:
            return lists[low]
        if low + 1 == high:
            return self.merge(lists[low], lists[high])
        
        mid = low + (high - low) // 2
        left = self.mergeKListsHelper(lists, low, mid)
        right = self.mergeKListsHelper(lists, mid + 1, high)
        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)

