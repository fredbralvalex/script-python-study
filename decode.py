#2[abc]3[cd]ef -> abcabccdcdcdef
def solution(str):
    stack = []
    token = ''
    num = 0
    for s in str:
        if s == '[':
            if token:
                stack.append(token)
                token = ''
            stack.append(num)
            num = 0

        elif s == ']':
            if token:
                stack.append(token)
                token = ''

            new_str = ''
            fst = stack.pop()
            while fst and type (fst) != int:
                new_str = fst + new_str
                fst = stack.pop()
            
            new_str = new_str * fst
            stack.append(new_str)

        else:
            if s.isdigit():
                num = 10 * num + int(s)
            else:
                token = token + s

    if token:
        stack.append(token)

    return ''.join(stack)

s = solution ("2[abc]3[cd]ef")
print(s)