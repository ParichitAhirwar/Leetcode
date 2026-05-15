class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        c=list(freq.values())
        return len(c)==len(set(c))