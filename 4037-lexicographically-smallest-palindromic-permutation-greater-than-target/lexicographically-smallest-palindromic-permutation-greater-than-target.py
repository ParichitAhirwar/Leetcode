class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = [i for i in range(26) if cnt[i] % 2]
        if len(odd) > 1:
            return ""

        mid = chr(ord('a') + odd[0]) if odd else ""

        half = [c // 2 for c in cnt]
        m = n // 2

        def build(left):
            return left + mid + left[::-1]

        tleft = target[:m]

        rem = half[:]
        possible_equal = True

        for ch in tleft:
            x = ord(ch) - ord('a')
            if rem[x] == 0:
                possible_equal = False
                break
            rem[x] -= 1

        if possible_equal:
            candidate = build(tleft)

            if candidate > target:
                return candidate

            for i in range(m - 1, -1, -1):
                rem = half[:]

                for j in range(i):
                    x = ord(tleft[j]) - ord('a')
                    rem[x] -= 1

                x = ord(tleft[i]) - ord('a')

                for c in range(x + 1, 26):
                    if rem[c] > 0:
                        rem[c] -= 1

                        left = tleft[:i] + chr(ord('a') + c)

                        for k in range(26):
                            left += chr(ord('a') + k) * rem[k]

                        return build(left)

            return ""

        for i in range(m - 1, -1, -1):
            rem = half[:]

            valid_prefix = True
            for j in range(i):
                x = ord(tleft[j]) - ord('a')
                if rem[x] == 0:
                    valid_prefix = False
                    break
                rem[x] -= 1

            if not valid_prefix:
                continue

            x = ord(tleft[i]) - ord('a')

            for c in range(x + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1

                    left = tleft[:i] + chr(ord('a') + c)

                    for k in range(26):
                        left += chr(ord('a') + k) * rem[k]
                    return build(left)
        return ""