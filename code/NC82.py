# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = set()
        nodeList = []
        while head:
            if head.val in dic:
                if head.val in nodeList:
                    nodeList.remove(head.val)
            else:
                dic.add(head.val)
                nodeList.append(head.val)
            head = head.next
        if nodeList:
            head = node = ListNode(nodeList[0])
            for i in range(1, len(nodeList)):
                node.next = ListNode(nodeList[i])
                node = node.next
        return head


obj = Solution()
node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(1)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(3)
# node.next.next.next.next.next = ListNode(4)
# node.next.next.next.next.next.next = ListNode(5)
print(obj.deleteDuplicates(node))