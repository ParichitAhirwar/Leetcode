class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Minimum item price
        min_price = min(price for factor, price in items)

        # Maximum factor
        M = max(factor for factor, price in items)

        # Frequency of each factor
        freq = [0] * (M + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count eligible item types for each factor
        divisible = [0] * (M + 1)

        for f in range(1, M + 1):
            for j in range(f, M + 1, f):
                divisible[f] += freq[j]

        # Collect useful free-copy opportunities
        opportunities = []

        for factor, price in items:
            count = divisible[factor] - 1
            extra = price - min_price

            if count > 0 and extra < min_price:
                opportunities.append((extra, count))

        # Cheapest extra cost first
        opportunities.sort()

        remaining = budget
        selected = 0
        extra_cost = 0

        # Select affordable premium purchases
        for extra, count in opportunities:
            # Each premium purchase costs min_price + extra
            cost = min_price + extra

            take = min(count, remaining // cost)

            selected += take
            remaining -= take * cost
            extra_cost += take * extra

        # Remaining budget can purchase ordinary copies
        normal = (budget - extra_cost) // min_price

        return normal + selected
