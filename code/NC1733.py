class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        learned = list(map(set, languages))
        todoList = set()
        for u, v in friendships:
            if learned[u - 1] & learned[v - 1]:
                continue
            todoList.add(u - 1)
            todoList.add(v - 1)

        cnt = [0] * (n + 1)
        for u in todoList:
            for v in languages[u]:
                cnt[v] += 1

        return len(todoList) - max(cnt)

