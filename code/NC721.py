class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_index = {}
        visited = [False] * len(accounts)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_index:
                    email_to_index[email] = [i]
                else:
                    email_to_index[email].append(i)

        def dfs(i):
            visited[i] = True
            for email in accounts[i][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_index[email]:
                    if not visited[j]:
                        dfs(j)
        ret = []
        for i, b in enumerate(visited):
            if not b:
                email_set = set()
                dfs(i)
                ret.append([accounts[i][0]] + sorted(email_set))

        return ret


obj = Solution()
print(obj.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                         ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
