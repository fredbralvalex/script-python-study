def solution(string):
    i = 0
    i0 = len(string) - 1
    while i <= i0:
        if not string[i] == string[i0]:
            return False
        else:
            i+=1
            i0-=1
    
    return True