def solution_n(_numbers, target_sum):
    numbers = list(sorted(_numbers)) 
    _len = len(numbers) - 1
    i = 0
    i0 = 1
    idx = _len
    response = []
    while i < idx:
        if i0 >= idx:
            i = i + 1
            i0 = i + 1
            idx = _len
        _sum = numbers[i] + numbers[i0] + numbers[idx]
        if _sum == target_sum:
            response.append([numbers[i], numbers[i0], numbers[idx]])
            idx = idx - 1
            i0 = i0 + 1
        elif _sum > target_sum:
            idx = idx - 1
        elif _sum < target_sum:
            i0 = i0 + 1
            
    return response

def solution_n2(numbers, target_sum):
    numbers.sort()
    _len = len(numbers) - 1
    i = 0
    i0 = 1
    idx = _len
    response = []
    while i < idx:
        while i0 < idx:
            _sum = numbers[i] + numbers[i0] + numbers[idx]
            if _sum == target_sum:
                response.append([numbers[i], numbers[i0], numbers[idx]])
                idx = idx - 1
                i0 = i0 + 1
            elif _sum > target_sum:
                idx = idx - 1
            elif _sum < target_sum:
                i0 = i0 + 1
        i = i + 1
        i0 = i + 1
        idx = _len
    return response

def solution_n3(numbers, target_sum):
    numbers.sort()
    response = []
    for i0 in range(len(numbers)- 2):
        el0 = numbers[i0]
        for i1 in range(i0 + 1, len(numbers)- 1):
            el1 = numbers[i1]
            for i2 in range(i1 + 1, len(numbers)):
                el2 = numbers[i2]
                if el0 + el1 + el2 == target_sum:
                    response.append([el0, el1, el2])

    return response

a = solution_n3([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(a)