def solution(string):
    i = 0
    i0 = len(string) - 1
    while i <= i0:
        if string[i] != string[i0]:
            return False
        else:
            i=i+1
            i0=i0-1
    
    return True

a = solution('algomania')
print(a)