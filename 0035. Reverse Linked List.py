"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        curt = None
        while(head != None):
            temp = head.next
            head.next = curt
            curt = head
            head = temp
            
        return curt
