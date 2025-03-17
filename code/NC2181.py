# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head.next
        head = pre = ListNode(0)
        while node:
            if node.val != 0:
                pre.val += node.val
            elif node.next:
                pre.next = ListNode(0)
                pre = pre.next
            node = node.next

        return head


obj = Solution()
head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
print(obj.mergeNodes(head))