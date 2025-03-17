class Solution(object):
    def fib(self, n):
        # 递归
        if 0 == n:
            return 0
        if 1 == n:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n):
        # 转移方程递推
        if n < 2:
            return n
        a1, a2, a3 = 0, 0, 1
        for i in range(2, n + 1):
            a1, a2 = a2, a3
            a3 = a1 + a2
        return a3

    def fib3(self, n):
        # 矩阵快速幂
