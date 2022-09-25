# A solucao deve estar implementada dentro da função abaixo.
# Dica: Você pode criar outras funções e classes se quiser mas esta é a função principal que será usada.


def solution(numbers, target_sum):
    return solution_nlogn(numbers, target_sum)
            
def solution_nlogn(numbers, target_sum):
    if not numbers or len(numbers) < 2:
        return []
    
    numbers.sort()   
    i = 0
    idx = len(numbers) - 1
    while i < idx:
        _sum = numbers[i] + numbers[idx]
        if _sum == target_sum:
            return [numbers[i], numbers[idx]]
        elif _sum > target_sum:
            idx = idx - 1
        else:
            i = i + 1
       
    return []


def solution_n(numbers, target_sum):
    if not numbers:
        return []
    my_dic = {}
    for num in numbers:
        val = target_sum - num
        if val in my_dic:
            return [val, num]
        else:
            my_dic[num] = val
    return []
    
def solution_n2(numbers, target_sum):
    idx = 0
    #for i in range(len(target))
    #for j in range(i + 1, len(target))
    for num in numbers:
        idx = idx + 1
        for num2 in numbers[idx: ]:
            if num + num2 == target_sum:
                return [num, num2]
    return []

solution_n([4, 1, 2, -2, 11, 15, 1, -1, -6, -4], 9 )    