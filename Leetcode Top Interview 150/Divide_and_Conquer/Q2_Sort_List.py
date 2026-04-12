# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2) :
        dummyNode = ListNode(-1)
        temp = dummyNode
        while list1 != None and list2 != None : 
            if list1.val <= list2.val :
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        if list1 != None :
            temp.next = list1
        else:
            temp.next = list2
        return dummyNode.next
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head
        
        prev=None
        slow=head 
        fast=head

        while fast != None and fast.next != None :
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)
    