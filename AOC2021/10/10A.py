with open('input.txt') as inp:
    s = inp.read()

stack = []

lefts = {'(','<','{','['}
points = {')':3,"]":57,"}":1197,'>':25137}

ans = 0

for line in s.split('\n'):
    for c in line:
        if c in lefts:
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                ans += points[c]
                break
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                ans += points[c]
                break
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                ans += points[c]
                break
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                ans += points[c]
                break
        else:
            print('error')
            exit(0)

print(ans)