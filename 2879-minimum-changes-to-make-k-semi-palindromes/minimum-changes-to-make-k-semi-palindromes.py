
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try every valid divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    m = length // d

                    # Check palindrome groups
                    for r in range(d):
                        left = i + r
                        right = i + r + (m - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):

                for p in range(2 * (parts - 1), i - 1):

                    if dp[p][parts - 1] == INF:
                        continue

                    if cost[p][i - 1] == INF:
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[p][parts - 1] + cost[p][i - 1]
                    )

        return dp[n][k]
