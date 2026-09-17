class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        left = 0
        current_sum = 0

        ans = float('inf')
        min_length = float('inf')

        for right in range(n):
            current_sum += arr[right]

            # Shrink window if sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            # If current window has sum == target
            if current_sum == target:
                length = right - left + 1

                # Check for a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Update minimum valid subarray length
                min_length = min(min_length, length)

            # Store best answer up to current index
            if right == 0:
                best[right] = min_length
            else:
                best[right] = min(best[right - 1], min_length)

        return -1 if ans == float('inf') else ans