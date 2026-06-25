class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        n = len(operations)

        for i in range(n):
            if operations[i] == "+":
                stk.append(stk[-1]+stk[-2])
            elif operations[i] == "C":
                stk.pop()
            elif operations[i] == "D":
                stk.append(stk[-1]*2)
            else:
                stk.append(int(operations[i]))

        return sum(stk)