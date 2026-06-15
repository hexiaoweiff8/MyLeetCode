# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmpHead = head
        array = [head]
        while tmpHead and tmpHead.next:
            tmpHead = tmpHead.next
            array.append(tmpHead)
        n = len(array)
        if n > 1:
            array[n // 2 - 1].next = array[n // 2].next
        return head if len(array) > 1 else None