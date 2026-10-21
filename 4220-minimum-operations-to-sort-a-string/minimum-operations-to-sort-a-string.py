class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        mx = max(s)
        mn = min(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        if s[0] != mx and s[-1] != mn:
            return 2

        if s[1:-1].count(mx) > 0 or s[1:-1].count(mn) > 0:
            return 2

        return 3