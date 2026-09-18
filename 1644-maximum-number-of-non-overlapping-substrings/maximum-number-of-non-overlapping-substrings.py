class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            valid = True

            i = left
            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character occurs before our interval
                if first[x] < left:
                    valid = False
                    break

                # Must include all occurrences of this character
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Select intervals with earliest ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans