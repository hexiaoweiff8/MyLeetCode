class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """

        ans = 0
        has_box = [False] * len(status)
        for box in initialBoxes:
            has_box[box] = True

        def dfs(index):
            nonlocal ans
            ans += candies[index]
            has_box[index] = False
            for key in keys[index]:
                status[key] = 1
                if has_box[key]:
                    dfs(key)
            for key in containedBoxes[index]:
                has_box[key] = True
                if status[key]:
                    dfs(key)

        for box in initialBoxes:
           if status[box] and has_box[box]:
               dfs(box)

        return ans



