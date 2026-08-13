class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char, _, prefix_a, suffix_a, best_a, len_a = a
            _, right_char, prefix_b, suffix_b, best_b, len_b = b

            prefix = prefix_a
            if prefix_a == len_a and left_char == b[0]:
                prefix = len_a + prefix_b

            suffix = suffix_b
            if suffix_b == len_b and a[1] == right_char:
                suffix = len_b + suffix_a

            best = max(best_a, best_b)

            if a[1] == b[0]:
                best = max(best, suffix_a + prefix_b)

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                len_a + len_b
            )

        def build(node, left, right):
            if left == right:
                tree[node] = (s[left], s[left], 1, 1, 1, 1)
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, pos, char):
            if left == right:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, char)
            else:
                update(node * 2 + 1, mid + 1, right, pos, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])  # best

        return ans