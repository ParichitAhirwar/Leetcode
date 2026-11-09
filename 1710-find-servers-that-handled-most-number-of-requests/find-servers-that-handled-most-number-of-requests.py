class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k
        for i in range(len(arrival)):
            curr_time = arrival[i]
            while busy and busy[0][0] <= curr_time:
                finish_time, server = heapq.heappop(busy)
                available.add(server)
            if not available:
                continue
            target = i % k
            idx = available.bisect_left(target)
            if idx == len(available):
                idx = 0
            server = available.pop(idx)
            count[server] += 1
            heapq.heappush(busy,(curr_time + load[i], server))
        max_count = max(count)
        return [ i for i in range(k) if count[i] == max_count]