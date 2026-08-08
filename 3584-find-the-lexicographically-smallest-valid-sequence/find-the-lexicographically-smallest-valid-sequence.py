class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        i = n - 1
        j = m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
        ans = []
        used_change = False
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not used_change:
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    used_change = True
        return ans if j == m else []