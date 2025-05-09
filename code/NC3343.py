# from functools import cache
#
#
# class Solution(object):
#     def countBalancedPermutations(self, num):
#         """
#         :type num: str
#         :rtype: int
#         """
#         @cache
#         def dfs(i, j, a, b):
#             if i > 9:
#                 return (j | a | b) == 0
#             if a == 0 and j:
#                 return 0
#             ans = 0
#             for l in range(min(cnt[i], a) + 1):
#                 r = cnt[i] - l
#                 if 0 <= r <= b and l * i <= j:
#                     t = comb(a)
#
#
#         cnt = Counter(num)