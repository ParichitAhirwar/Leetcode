from heapq import heappush, heappop

class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        K = self.log[self.n] + 1
        self.st_max = [[0] * K for _ in range(self.n)]
        self.st_min = [[0] * K for _ in range(self.n)]
        for i in range(self.n):
            self.st_max[i][0] = nums[i]
            self.st_min[i][0] = nums[i]
        j = 1
        while (1 << j) <= self.n:
            length = 1 << j
            half = length >> 1
            for i in range(self.n - length + 1):
                self.st_max[i][j] = max(
                    self.st_max[i][j - 1],
                    self.st_max[i + half][j - 1]
                )
                self.st_min[i][j] = min(
                    self.st_min[i][j - 1],
                    self.st_min[i + half][j - 1]
                )
            j += 1

    def query_max(self, l, r):
        k = self.log[r - l + 1]
        return max(
            self.st_max[l][k],
            self.st_max[r - (1 << k) + 1][k]
        )

    def query_min(self, l, r):
        k = self.log[r - l + 1]
        return min(
            self.st_min[l][k],
            self.st_min[r - (1 << k) + 1][k]
        )

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTable(nums)
        def value(l, r):
            return st.query_max(l, r) - st.query_min(l, r)
        heap = []
        for l in range(n):
            val = value(l, n - 1)
            heappush(heap, (-val, l, n - 1))
        ans = 0
        for _ in range(k):
            neg_val, l, r = heappop(heap)
            val = -neg_val
            ans += val
            if r > l:
                nxt = value(l, r - 1)
                heappush(heap, (-nxt, l, r - 1))
        return ans