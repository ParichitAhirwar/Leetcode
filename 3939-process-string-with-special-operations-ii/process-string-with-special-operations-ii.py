class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        len_after = [0] * (n + 1)
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                len_after[i + 1] = len_after[i] + 1
            elif ch == '*':
                len_after[i + 1] = max(0, len_after[i] - 1)
            elif ch == '#':
                len_after[i + 1] = len_after[i] * 2
            else: 
                len_after[i + 1] = len_after[i]
        if k >= len_after[n]:
            return '.'
        idx = k
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = len_after[i]
            if 'a' <= ch <= 'z':
                if idx == prev_len:
                    return ch
            elif ch == '#':
                if idx >= prev_len:
                    idx -= prev_len
            elif ch == '%':
                idx = prev_len - 1 - idx
            else: 
                pass
        return '.'