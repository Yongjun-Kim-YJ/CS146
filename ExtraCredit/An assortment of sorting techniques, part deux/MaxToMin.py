import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def extract_min(self):
        return -heapq.heappop(self.heap)

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
print(min_heap.extract_min())
print(min_heap.extract_min())
print(min_heap.extract_min())
