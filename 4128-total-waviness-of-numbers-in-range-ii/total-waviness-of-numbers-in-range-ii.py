class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(N: int) -> int:
            if N < 0:
                return 0
            digits = list(map(int, str(N)))
            L = len(digits)
            @lru_cache(None)
            def dfs(pos, tight, k, prev2, prev1):
                if pos == L:
                    return (1, 0) 
                limit = digits[pos] if tight else 9
                total_cnt = 0
                total_wavy = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if k == 0:
                        if d == 0:
                            cnt, wav = dfs(pos + 1, ntight, 0, 0, 0)
                        else:
                            cnt, wav = dfs(pos + 1, ntight, 1, 0, d)
                        total_cnt += cnt
                        total_wavy += wav
                    elif k == 1:
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)
                        total_cnt += cnt
                        total_wavy += wav
                    else: 
                        is_extreme = (
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        )
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)
                        total_cnt += cnt
                        total_wavy += wav + is_extreme * cnt
                return (total_cnt, total_wavy)
            return dfs(0, True, 0, 0, 0)[1]
        return solve(num2) - solve(num1 - 1)