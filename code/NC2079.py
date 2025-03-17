class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        cap = capacity
        for i in range(len(plants)):
            if plants[i] > cap:
                steps += 2 * i
                cap = capacity
            steps += 1
            cap -= plants[i]
        return steps