import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def extract_max(self):
        return -heapq.heappop(self.heap)

max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
print(max_heap.extract_max())
print(max_heap.extract_max())
print(max_heap.extract_max())
