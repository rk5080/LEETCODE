# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fastp = head
        slowp = head
        N = n
    # Move the fastp pointer N nodes ahead
        for i in range(N):
            fastp = fastp.next

    # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

    # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

    # Delete the Nth node from the end
        #delNode = slowp.next
        slowp.next = slowp.next.next
        #delNode = None
        return head

# The following is brute force
        """
        node = head
        i = 1
        while node.next:
            node = node.next
            i = i+1
        node1 = head
        if i - n==0:
            head = node1.next
            return head
        j = 1
        while node1:
            if j == i-n:
                node1.next = node1.next.next
            node1 = node1.next
            j += 1
        #node1.next = None
        return head
        """

        