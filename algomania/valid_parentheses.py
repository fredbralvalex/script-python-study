def solution(str):
    stack = []
    mapping = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for s in str:
        if s in mapping:
            if len(stack) and mapping[s] == stack.pop():
                continue
            stack.append(s)

    return len(stack) == 0

s = solution('[]{}[]()')
print(s)