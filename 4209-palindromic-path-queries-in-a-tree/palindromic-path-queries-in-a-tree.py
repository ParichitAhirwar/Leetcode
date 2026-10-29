class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # 1. Calculate subtree sizes and heavy children.
        order = [0]
        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # 2. Heavy-Light Decomposition.
        head = [0] * n
        pos = [0] * n
        rev = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                rev[timer] = u
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # 3. Segment tree storing character parity masks.
        seg = [0] * (4 * n)

        def build(node, left, right):
            if left == right:
                seg[node] = 1 << (ord(s[rev[left]]) - ord('a'))
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]

        def update(node, left, right, p, mask):
            if left == right:
                seg[node] = mask
                return

            mid = (left + right) // 2
            if p <= mid:
                update(node * 2, left, mid, p, mask)
            else:
                update(node * 2 + 1, mid + 1, right, p, mask)

            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]

        def range_query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return seg[node]

            mid = (left + right) // 2
            result = 0

            if ql <= mid:
                result ^= range_query(
                    node * 2, left, mid, ql, qr
                )
            if qr > mid:
                result ^= range_query(
                    node * 2 + 1, mid + 1, right, ql, qr
                )

            return result

        build(1, 0, n - 1)

        # 4. XOR masks along the path between u and v.
        def path_query(u, v):
            mask = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                mask ^= range_query(
                    1, 0, n - 1, pos[head[u]], pos[u]
                )
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            mask ^= range_query(
                1, 0, n - 1, pos[u], pos[v]
            )
            return mask

        # 5. Process queries.
        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                chars[u] = c
                update(
                    1, 0, n - 1, pos[u],
                    1 << (ord(c) - ord('a'))
                )
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_query(u, v)

                # At most one character may have odd frequency.
                answer.append((mask & (mask - 1)) == 0)

        return answer