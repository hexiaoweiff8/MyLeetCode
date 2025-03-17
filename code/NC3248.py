class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        x, y = 0, 0
        for i in range(len(commands)):
            if commands[i] == 'UP':
                y -= 1
            elif commands[i] == 'DOWN':
                y += 1
            elif commands[i] == 'LEFT':
                x -= 1
            else:
                x += 1
        return (y * n) + x