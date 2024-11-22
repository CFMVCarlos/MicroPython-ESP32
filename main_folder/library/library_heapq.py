import heapq

# Example heap
heap = []

# Pushing items onto the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)

print("Heap after pushing items:", heap)

# Popping items from the heap
while heap:
    smallest = heapq.heappop(heap)
    print("Popped:", smallest)

# Example list
x = [4, 6, 1, 8, 3, 9, 2]

# Convert the list into a heap
heapq.heapify(x)
print("Heapified list:", x)
while x:
    smallest = heapq.heappop(x)
    print("Popped:", smallest)
