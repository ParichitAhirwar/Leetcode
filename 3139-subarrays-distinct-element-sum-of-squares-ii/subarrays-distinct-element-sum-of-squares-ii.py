class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores:
        # sum1 = sum of distinct counts
        # sum2 = sum of squared distinct counts
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, delta):
            length = r - l + 1

            # (x + delta)^2 = x^2 + 2*delta*x + delta^2
            sum2[node] = (
                sum2[node]
                + 2 * delta * sum1[node]
                + delta * delta * length
            ) % MOD

            sum1[node] = (
                sum1[node] + delta * length
            ) % MOD

            lazy[node] += delta

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            delta = lazy[node]

            apply(node * 2, l, mid, delta)
            apply(node * 2 + 1, mid + 1, r, delta)

            lazy[node] = 0

        def update(node, l, r, ql, qr, delta):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                apply(node, l, r, delta)
                return

            push(node, l, r)
            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr, delta)
            update(node * 2 + 1, mid + 1, r, ql, qr, delta)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD

            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0

            if ql <= l and r <= qr:
                return sum2[node]

            push(node, l, r)
            mid = (l + r) // 2

            return (
                query(node * 2, l, mid, ql, qr)
                + query(node * 2 + 1, mid + 1, r, ql, qr)
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            # Increase distinct counts for subarrays
            # starting after the previous occurrence of x.
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, r, 1)

            # Add squared distinct counts for subarrays
            # ending at r.
            ans = (ans + query(1, 0, n - 1, 0, r)) % MOD

            last[x] = r

        return ans