MOD = 10**9 + 7
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        # A[i][j] = min(i+1, j+1) - 1
        A = [[min(i + 1, j + 1) - 1 for j in range(m)] for i in range(m)]

        def mat_mul(X, Y):
            n = len(X)
            Z = [[0] * n for _ in range(n)]

            for i in range(n):
                Xi = X[i]
                Zi = Z[i]
                for k in range(n):
                    if Xi[k] == 0:
                        continue
                    x = Xi[k]
                    Yk = Y[k]
                    for j in range(n):
                        if Yk[j]:
                            Zi[j] = (Zi[j] + x * Yk[j]) % MOD
            return Z

        def mat_pow(base, exp):
            n = len(base)
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                res[i][i] = 1

            while exp:
                if exp & 1:
                    res = mat_mul(res, base)
                base = mat_mul(base, base)
                exp >>= 1

            return res

        def mat_vec_mul(M, v):
            n = len(M)
            res = [0] * n

            for i in range(n):
                s = 0
                row = M[i]
                for j in range(n):
                    s = (s + row[j] * v[j]) % MOD
                res[i] = s

            return res

        if n % 2 == 0:
            # U2[i] = i
            U = [i for i in range(m)]
            P = mat_pow(A, (n - 2) // 2)
            U = mat_vec_mul(P, U)
        else:
            # U3[i] = i*m - i*(i+1)//2
            U = [(i * m - i * (i + 1) // 2) % MOD for i in range(m)]
            P = mat_pow(A, (n - 3) // 2)
            U = mat_vec_mul(P, U)

        return (2 * sum(U)) % MOD