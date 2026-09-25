class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def union(a, b):
            return a | b

        def concat(a, b):
            return {x + y for x in a for y in b}

        def parse_expr(i):
            """
            Parse a sequence until ',' or '}'.
            Returns: (next_index, set_of_words)
            """
            res = {""}

            while i < n and expression[i] not in ",}":
                if expression[i].islower():
                    cur = {expression[i]}
                    i += 1
                else:
                    # expression[i] == '{'
                    i, cur = parse_group(i + 1)

                res = concat(res, cur)

            return i, res

        def parse_group(i):
            """
            Parse contents after '{'.
            Returns: (index after '}', set_of_words)
            """
            res = set()

            while True:
                i, cur = parse_expr(i)
                res.update(cur)

                if expression[i] == '}':
                    return i + 1, res

                # expression[i] == ','
                i += 1

        _, ans = parse_expr(0)

        return sorted(ans)