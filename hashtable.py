def solution(numbers, k):
    return solution_n(numbers, k)

def solution_nlogn(numbers, k):
    map = {}
    for i in range(len(numbers)):
        if numbers[i] in map:
            map[numbers[i]] = map[numbers[i]] + 1
        else:
            map[numbers[i]] = 1

    pairs = sorted(map.items(), key = lambda x: x[1], reverse=True)
    result = []
    for pair in pairs[:k]:
        result.append(pair[0])
    return result

import heapq
def solution_nlogk(numbers, k):
    map = {}
    for i in range(len(numbers)):
        if numbers[i] in map:
            map[numbers[i]] = map[numbers[i]] + 1
        else:
            map[numbers[i]] = 1

    heap = []
    for num, count in map.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap) 

    result = []
    for pair in heap:
        result.append(pair[1])
    return result

def solution_n(numbers, k):
    map = {}
    for i in range(len(numbers)):
        if numbers[i] in map:
            map[numbers[i]] = map[numbers[i]] + 1
        else:
            map[numbers[i]] = 1
    
    freq = {}
    for num,count in map.items():
        if count not in freq:
            freq[count] = []
        freq[count].append(num)
    
    result = []
    for i in reversed(range(len(numbers)+1)):
        if i in freq:
            result.extend(freq[i])

    return result[:k]

s = solution([1, 1, 1, 3, 3, 5, 5, 5, 6, 7, 8, 9, 10], 2)
print(s)