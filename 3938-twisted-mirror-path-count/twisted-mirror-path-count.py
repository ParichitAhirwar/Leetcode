class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Number of paths entering each cell from left and above.
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Start at (0, 0).
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (right[i][j] + down[i][j]) % MOD

                if grid[i][j] == 0:
                    # Empty cell: continue in either direction.
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD

                else:
                    # Mirror: direction changes.
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD