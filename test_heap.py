import heapq

heap = [1, 2, 65, 78, 98, 3, 6, 7, 99]

h = heapq.heapify(heap)

print(h)
heapq.heapify(heap)
[1, 2, 3, 7, 98, 65, 6, 78, 99]
heapq.nlargest(3, heap) 
[99, 98, 78]
heapq.nsmallest(3, heap) 
[1, 2, 3]
heapq.heappush(heap, -9)  
heap
[-9, 1, 3, 7, 2, 65, 6, 78, 99, 98]
heapq.heappop(heap) 
-9
heap
[1, 2, 3, 7, 98, 65, 6, 78, 99]
heapq.heappushpop(heap, 12) 
1
heap
[2, 7, 3, 12, 98, 65, 6, 78, 99]
heap[0] 
2
heapq.nlargest(1, heap) 
[99]
