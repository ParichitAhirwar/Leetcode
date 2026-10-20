class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        # Precompute adjacent descents.
        desc = [0] * (n + 1)
        for i in range(n - 1):
            desc[i + 1] = desc[i] + (nums[i] > nums[i + 1])
        desc[n] = desc[n - 1]

        # Try each divisor of n.
        for k in range(1, n + 1):
            if n % k:
                continue

            valid = True
            prev_max = float("-inf")

            for start in range(0, n, k):
                end = start + k

                # Number of descents inside the block.
                drops = desc[end - 1] - desc[start]

                # Include the circular boundary.
                if nums[end - 1] > nums[start]:
                    drops += 1

                if drops > 1:
                    valid = False
                    break

                block_min = min(nums[start:end])
                block_max = max(nums[start:end])

                if prev_max > block_min:
                    valid = False
                    break

                prev_max = block_max

            if valid:
                ans += k

        return ans