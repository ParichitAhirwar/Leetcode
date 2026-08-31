from functools import lru_cache


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # ---------------------------------------------------------
        # Factorize t into 2, 3, 5, 7
        # ---------------------------------------------------------
        e2 = e3 = e5 = e7 = 0

        while t % 2 == 0:
            e2 += 1
            t //= 2

        while t % 3 == 0:
            e3 += 1
            t //= 3

        while t % 5 == 0:
            e5 += 1
            t //= 5

        while t % 7 == 0:
            e7 += 1
            t //= 7

        # A digit 1..9 cannot produce any other prime factor.
        if t != 1:
            return "-1"

        # ---------------------------------------------------------
        # Factor contribution of each digit
        # ---------------------------------------------------------
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # ---------------------------------------------------------
        # Minimum number of digits needed to satisfy a factor state
        # ---------------------------------------------------------
        INF = 10**9

        @lru_cache(None)
        def min_digits(a, b, c, d):

            if a == 0 and b == 0 and c == 0 and d == 0:
                return 0

            ans = INF

            for digit in (2, 3, 4, 5, 6, 7, 8, 9):

                x2, x3, x5, x7 = factors[digit]

                na = max(0, a - x2)
                nb = max(0, b - x3)
                nc = max(0, c - x5)
                nd = max(0, d - x7)

                # This digit must reduce the requirement.
                if (na, nb, nc, nd) == (a, b, c, d):
                    continue

                ans = min(
                    ans,
                    1 + min_digits(na, nb, nc, nd)
                )

            return ans

        # ---------------------------------------------------------
        # Construct lexicographically smallest number of EXACTLY
        # 'length' digits satisfying the requirements.
        # ---------------------------------------------------------
        def build(a, b, c, d, length):

            if min_digits(a, b, c, d) > length:
                return None

            result = []

            for pos in range(length):

                remaining = length - pos - 1

                for digit in range(1, 10):

                    x2, x3, x5, x7 = factors[digit]

                    na = max(0, a - x2)
                    nb = max(0, b - x3)
                    nc = max(0, c - x5)
                    nd = max(0, d - x7)

                    if min_digits(na, nb, nc, nd) <= remaining:

                        result.append(str(digit))

                        a, b, c, d = na, nb, nc, nd

                        break

                else:
                    return None

            return ''.join(result)

        n = len(num)

        # ---------------------------------------------------------
        # Check if num itself is already a valid answer
        # ---------------------------------------------------------
        if '0' not in num:

            a = b = c = d = 0

            for ch in num:

                x2, x3, x5, x7 = factors[int(ch)]

                a += x2
                b += x3
                c += x5
                d += x7

            if (
                a >= e2 and
                b >= e3 and
                c >= e5 and
                d >= e7
            ):
                return num

        # ---------------------------------------------------------
        # Prefix factor counts
        # ---------------------------------------------------------
        pref = [[0, 0, 0, 0] for _ in range(n + 1)]
        zero = [False] * (n + 1)

        for i, ch in enumerate(num):

            digit = int(ch)

            pref[i + 1] = pref[i].copy()

            x2, x3, x5, x7 = factors[digit]

            pref[i + 1][0] += x2
            pref[i + 1][1] += x3
            pref[i + 1][2] += x5
            pref[i + 1][3] += x7

            zero[i + 1] = zero[i] or digit == 0

        # ---------------------------------------------------------
        # CASE 1:
        # Same length as num.
        #
        # Change the RIGHTMOST possible position.
        # ---------------------------------------------------------
        for i in range(n - 1, -1, -1):

            # Prefix must be zero-free.
            if zero[i]:
                continue

            current = int(num[i])

            # Try smallest digit greater than current.
            for digit in range(current + 1, 10):

                x2, x3, x5, x7 = factors[digit]

                used2 = pref[i][0] + x2
                used3 = pref[i][1] + x3
                used5 = pref[i][2] + x5
                used7 = pref[i][3] + x7

                a = max(0, e2 - used2)
                b = max(0, e3 - used3)
                c = max(0, e5 - used5)
                d = max(0, e7 - used7)

                remaining = n - i - 1

                if min_digits(a, b, c, d) <= remaining:

                    suffix = build(
                        a, b, c, d, remaining
                    )

                    if suffix is not None:
                        return (
                            num[:i]
                            + str(digit)
                            + suffix
                        )

        # ---------------------------------------------------------
        # CASE 2:
        # Need a longer number.
        #
        # The smallest possible length is:
        # max(n + 1, minimum required digits)
        # ---------------------------------------------------------
        minimum_length = min_digits(e2, e3, e5, e7)

        length = max(n + 1, minimum_length)

        return build(
            e2,
            e3,
            e5,
            e7,
            length
        ) or "-1"