class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        # Inserting copy nodes in between
        temp = head
        while temp:
            p = Node(temp.val)
            p.next = temp.next
            temp.next = p
            temp = p.next

        # Updating the random pointer
        temp = head
        while temp:
            if temp.random != None:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next

        # Updating the next pointer
        newhead = head.next
        dummy = head.next
        temp = head
        while temp:
            if temp.next != None:
                temp.next = temp.next.next
            if dummy.next != None:
                dummy.next = dummy.next.next
            temp = temp.next
            dummy = dummy.next
        return newhead
        