class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(height) - 1):
            if height[i] > threshold:
                result.append(i + 1)
        return result
        return [i + 1 for i in range(0, len(height) - 1) if height[i] > threshold]
