# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prePreVal = head.val
        preVal = head.next.val
        head = head.next.next
        index = 1
        lastIndex = 0
        firstIndex = 0
        minGap = 999999
        while head:
            if head.val < preVal > prePreVal or head.val > preVal < prePreVal:
                print(index, head.val, preVal, prePreVal)
                if not firstIndex:
                    firstIndex = index
                if lastIndex:
                    minGap = min(index - lastIndex, minGap)
                lastIndex = index
            prePreVal = preVal
            preVal = head.val
            head = head.next
            index += 1
        if minGap == 999999:
            return [-1, -1]
        return [minGap, lastIndex - firstIndex]

