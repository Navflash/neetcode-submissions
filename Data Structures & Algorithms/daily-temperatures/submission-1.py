class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i,t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                sT,sI = stk.pop()
                res[sI] = i - sI

            stk.append((t,i))

        return res

