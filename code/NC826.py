from bisect import bisect_left


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        dAndP = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        dAndP.sort(key=lambda x: x[1])
        res = 0
        for workerNum in worker:
            i = bisect_left(dAndP, [workerNum, 999999999999999]) - 1
            if i >= 0:
                res += dAndP[i][1]

        return res

    def maxProfitAssignment2(self, difficulty, profit, worker):
        dAndP = sorted(zip(difficulty, profit))
        i = res = maxVal = 0
        worker.sort()
        for workerNum in worker:
            while i < len(dAndP) and dAndP[i][0] <= workerNum:
                maxVal = max(maxVal, dAndP[i][1])
                i += 1
            res += maxVal
        return res

obj = Solution()
print(obj.maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]))
print(obj.maxProfitAssignment(difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]))
