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
        if l1.val == 0:
            return l2
        s1, s2 = [], []
        carry = 0
        ret = None
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        while s1 or s2 or carry != 0:
            val = 0
            val += s1.pop() if s1 else 0
            val += s2.pop() if s2 else 0
            val += carry
            carry = val // 10
            val %= 10
            newNode = ListNode(val)
            newNode.next = ret
            ret = newNode

        return ret
