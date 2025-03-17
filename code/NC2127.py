from collections import deque


class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        deg = [0] * n
        for i in favorite:
            # 统计入度
            deg[i] += 1

        # 反图
        rg = [[] for _ in range(n)]
        # 完全不相连的点
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            # 减掉入度为0的点
            x = q.popleft()
            y = favorite[x]
            rg[y].append(x)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        # 反图中查找最深的链
        def rdfs(x):
            max_depth = 1
            for son in rg[x]:
                max_depth = max(max_depth, rdfs(son) + 1)
            return max_depth

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0:
                continue
            # 遍历基环上的点, 并标为0防止重复访问
            deg[i] = 0
            ring_size = 1
            x = favorite[i]
            while x != i:
                # 遍历基环上的点, 并标为0防止重复访问
                deg[x] = 0
                ring_size += 1
                x = favorite[x]
            if ring_size == 2:
                # 累加前后环大小
                sum_chain_size += rdfs(i) + rdfs(favorite[i])
            else:
                # 获取最大环
                max_ring_size = max(max_ring_size, ring_size)
        return max(max_ring_size, sum_chain_size)

