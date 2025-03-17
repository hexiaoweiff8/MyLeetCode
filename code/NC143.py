# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        tmpHead, list = head, []
        while tmpHead:
            list.append(tmpHead)
            tmpHead = tmpHead.next
        left, right = 1, len(list) - 1
        tmpHead = head
        while left <= right:
            tmpHead.next = list[right]
            if left != right:
                tmpHead.next.next = list[left]
                if tmpHead.next.next:
                    tmpHead.next.next.next = None
                tmpHead = tmpHead.next.next
            else:
                if tmpHead.next:
                    tmpHead.next.next = None
                tmpHead = tmpHead.next
            right -= 1
            left += 1
        return head


obj = Solution()
head = [1,2,3,4]
tmpNode = ListNode()
node = tmpNode
for item in head:
    tmpNode.next = ListNode()
    tmpNode.next.val = item
    tmpNode = tmpNode.next
print(obj.reorderList(node.next))
