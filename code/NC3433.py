class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        dic = {}
        for user in range(numberOfUsers):
            dic['id' + str(user)] = 0

        for event in events:
            if event[0] == "MESSAGE":
                idsArray = event[2].split(" ")
                for id in idsArray:
                    dic[id] += 1
            elif event[0] == "OFFLINE":
                dic['id' + event[2]] +=