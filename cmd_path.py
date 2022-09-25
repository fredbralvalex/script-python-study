def solution(path):
    i0 = 0
    stack = []

    if path[-1] != '/':
        path+= '/'
        
    for i in range(len(path)):
        if path[i] == '/':
            current = path[i0:i]
            i0 = i

            if current:
                if current == '/..':
                    if stack:
                        stack.pop()
                elif current == '/.' or current == '/':
                    continue
                else:
                    stack.append(current)
    if not stack:
        stack.append('/')

    return ''.join(stack)

s = solution('/home/../home/etc/.././url')
print(s)