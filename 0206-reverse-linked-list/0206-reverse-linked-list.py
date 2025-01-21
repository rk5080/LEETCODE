class Solution(object):
    def reverseList(self, head):        
        #Iterative method
        node = head
        temp = None
        while node is not None:
            y = node.next
            node.next = temp
            temp = node
            node = y
        return temp
        
        """ #Recursive method
        if head is None or head.next is None:
            return head
        new_head = reverseList(self,head.next)
        y = head.next
        y.next = head
        head.next = None
        return new_head
        """
        
        
        
        """
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
        """