class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Segment tree:
        # prod[node] = product of the whole segment modulo k
        # cnt[node][r] = number of non-empty prefixes
        #               having product % k == r
        size = 4 * n

        prod = [0] * size
        cnt = [[0] * k for _ in range(size)]

        def make_leaf(node, value):
            value %= k
            prod[node] = value
            cnt[node] = [0] * k
            cnt[node][value] = 1

        def merge(left, right):
            p1 = prod[left]
            p2 = prod[right]

            new_prod = (p1 * p2) % k
            new_cnt = [0] * k

            # Prefixes entirely inside left
            for r in range(k):
                new_cnt[r] += cnt[left][r]

            # Prefixes consisting of all left + prefix of right
            for r in range(k):
                if cnt[right][r]:
                    new_r = (p1 * r) % k
                    new_cnt[new_r] += cnt[right][r]

            return new_prod, new_cnt

        def build(node, l, r):
            if l == r:
                make_leaf(node, nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            prod[node], cnt[node] = merge(node * 2, node * 2 + 1)

        def update(node, l, r, idx, value):
            if l == r:
                make_leaf(node, value)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            prod[node], cnt[node] = merge(node * 2, node * 2 + 1)

        # Return (product, prefix-count-array) for a range.
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], cnt[node][:]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left_prod, left_cnt = query(
                node * 2, l, mid, ql, qr
            )
            right_prod, right_cnt = query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

            # Merge two returned ranges.
            new_prod = (left_prod * right_prod) % k
            new_cnt = [0] * k

            # Prefixes entirely in left part
            for r in range(k):
                new_cnt[r] += left_cnt[r]

            # Prefixes containing all left + prefix of right
            for r in range(k):
                new_r = (left_prod * r) % k
                new_cnt[new_r] += right_cnt[r]

            return new_prod, new_cnt

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # This update persists for all future queries.
            update(1, 0, n - 1, index, value)

            # We need all possible non-empty prefixes of
            # nums[start ... n-1].
            _, prefix_counts = query(
                1, 0, n - 1, start, n - 1
            )

            ans.append(prefix_counts[x])

        return ans