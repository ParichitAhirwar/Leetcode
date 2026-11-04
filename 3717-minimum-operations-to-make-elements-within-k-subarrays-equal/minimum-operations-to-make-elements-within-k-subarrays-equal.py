from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        low = SortedList()
        high = SortedList()

        sum_low = 0
        sum_high = 0

        def balance():
            nonlocal sum_low, sum_high

            while len(low) > len(high) + 1:
                v = low.pop()
                sum_low -= v
                high.add(v)
                sum_high += v

            while len(low) < len(high):
                v = high.pop(0)
                sum_high -= v
                low.add(v)
                sum_low += v

        def add(v):
            nonlocal sum_low, sum_high

            if not low or v <= low[-1]:
                low.add(v)
                sum_low += v
            else:
                high.add(v)
                sum_high += v

            balance()

        def remove(v):
            nonlocal sum_low, sum_high

            if low and v <= low[-1]:
                low.remove(v)
                sum_low -= v
            else:
                high.remove(v)
                sum_high -= v

            balance()

        def get_cost():
            median = low[-1]

            return (
                median * len(low) - sum_low
                + sum_high - median * len(high)
            )

        # Step 1: Calculate all window costs.
        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        # Step 2: DP
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element.
                curr[i] = curr[i - 1]

                # Choose window [i-x, i-1].
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]