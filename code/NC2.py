# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newNode = ListNode()
        newNodeFisrt = newNode
        l1Val = l1
        l2Val = l2
        isPlus = False
        while l1Val or l2Val:
            val = 0
            if l1Val and l2Val:
                val = l1Val.val + l2Val.val + (1 if isPlus else 0)
                newNode.val = val % 10
                if val >= 10 or l1Val.next or l2Val.next:
                    newNode.next = ListNode()
                    newNode = newNode.next
                l1Val = l1Val.next
                l2Val = l2Val.next
            elif l1Val or l2Val:
                lVal = l1Val if l1Val else l2Val
                val = lVal.val + (1 if isPlus else 0)
                newNode.val = val % 10
                if val >= 10 or lVal.next:
                    newNode.next = ListNode()
                    newNode = newNode.next
                if l1Val:
                    l1Val = l1Val.next
                elif l2Val:
                    l2Val = l2Val.next

            if val >= 10:
                isPlus = True
            else:
                isPlus = False
        if isPlus:
            newNode.val += 1

        return newNodeFisrt


obj = Solution()
l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1.next.val = 4
l1.next.next = ListNode()
l1.next.next.val = 3
l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2.next.val = 6
l2.next.next = ListNode()
l2.next.next.val = 6
print(obj.addTwoNumbers(l1, l2))
