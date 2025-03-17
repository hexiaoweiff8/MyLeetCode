# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        list1FirstNode = list1
        list2FirstNode = list2
        subNode1 = subNode2 = None
        index = 0
        # 获取list2的最后节点
        while list2FirstNode.next:
            list2FirstNode = list2FirstNode.next
        listEndNode = list2FirstNode

        # 获取list1中的两个节点
        while list1FirstNode.next:
            if a == index - 1:
                subNode1 = list1FirstNode
            elif index == b:
                subNode2 = list1FirstNode

            list1FirstNode = list1FirstNode.next
            index += 1
        subNode1.next = list2
        listEndNode.next = subNode2
        return list1


obj = Solution()
print(obj.mergeInBetween([0, 1, 2, 3, 4, 5, 6], 2, 5, [1000000, 1000001, 1000002, 1000003, 1000004]))
