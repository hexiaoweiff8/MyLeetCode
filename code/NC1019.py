# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        vals = []
        ret = []
        index = 0
        while head:
            ret.append(0)
            while vals and vals[-1][0] < head.val:
                ret[vals[-1][1]] = head.val
                vals.pop()
            vals.append([head.val, index])
            head = head.next
            index += 1


        #
        # maxVal = -1
        # lenVals = len(vals)
        # for index in range(lenVals - 1, -1, -1):
        #     val = vals[index]
        #     if 0 < index < lenVals - 1 and vals[index - 1] < val > vals[index + 1]:
        #         ret.insert(0, maxVal if maxVal > val else 0)
        #         maxVal = val
        #     elif maxVal <= val:
        #         maxVal = val
        #         ret.insert(0, 0)
        #     else:
        #         ret.insert(0, maxVal)

        return ret


obj = Solution()
# listNode = ListNode()
# listNode.val = 2
# listNode.next = ListNode()
# listNode.next.val = 7
# listNode.next.next = ListNode()
# listNode.next.next.val = 4
# listNode.next.next.next = ListNode()
# listNode.next.next.next.val = 3
# listNode.next.next.next.next = ListNode()
# listNode.next.next.next.next.val = 5
# print(obj.nextLargerNodes(listNode))

# lst = [1,7,5,1,9,2,5,1]
lst = [3, 3]
listNode = ListNode()
firstNode = listNode
for index in range(len(lst)):
    item = lst[index]
    listNode.val = item
    if index < len(lst) - 1:
        listNode.next = ListNode()
        listNode = listNode.next
print(obj.nextLargerNodes(firstNode))
