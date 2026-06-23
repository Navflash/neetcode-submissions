class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        n1 = len(word1)
        n2 = len(word2)

        while i < n1 and j < n2:
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1


        while i == n1 and j < n2:
            res.append(word2[j])
            j+=1

        while i < n1 and j == n2:
            res.append(word1[i])
            i+=1

        return "".join(res)