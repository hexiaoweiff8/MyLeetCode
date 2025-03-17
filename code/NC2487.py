# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = node = head
        preNode = None
        lastNode = None
        while node:
            node.pre = preNode
            preNode = node
            node = node.next
            if node is None:
                lastNode = preNode
        while lastNode and lastNode.pre:
            if lastNode.val > lastNode.pre.val:
                if lastNode.pre.pre:
                    lastNode.pre.pre.next = lastNode.pre.next
                    lastNode.pre = lastNode.pre.pre
                else:
                    ret = lastNode
                    break
            else:
                lastNode = lastNode.pre

        return ret


obj = Solution()
# [5,2,13,3,8]
node = ListNode(5)
node.next = ListNode(2)
node.next.next = ListNode(13)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(8)
print(obj.removeNodes(node))