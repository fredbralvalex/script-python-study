def solution(str):
    result = 0
    value = ''
    for i in range(len(str)):
        map = {str[i] : True}
        i0 = i

        while True:
            i0 = i0 + 1
            if i0 >= len(str) or str[i0] in map:
                if len(map.keys()) > result:
                    value = ''.join(map.keys())
                result = max(len(map.keys()), result)
                break

            map[str[i0]] = True
    print(value)
    return result

s = solution('zzzabcdadjhj')
print(s)