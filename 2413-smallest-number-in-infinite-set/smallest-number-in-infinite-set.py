class SmallestInfiniteSet:

    def __init__(self):
        self.current=1
        self.heap=[]
        self.in_heap=set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest=heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        ans=self.current
        self.current+=1
        return ans

    def addBack(self, num: int) -> None:
        if num<self.current and num not in self.in_heap:
            heapq.heappush(self.heap,num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)