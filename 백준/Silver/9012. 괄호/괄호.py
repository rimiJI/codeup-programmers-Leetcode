a = int(input())

def check(bracket_elements):
    stack = []  
    for char in bracket_elements:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

for _ in range(a):
    brackets = input().strip()
    result = check(brackets)
    print(result)