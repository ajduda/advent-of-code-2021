with open('input.txt') as inp:
    s = inp.read()


lefts = {'(','<','{','['}
points = {'(':1,"[":2,"{":3,'<':4}

scores = []

for line in s.split('\n'):
    lineAns = 0
    stack = []
    bad = False
    for c in line:
        if c in lefts:
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                bad = True
                break
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                bad = True
                break
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                bad = True
                break
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                bad = True
                break
        else:
            print('error')
            exit(0)
    if bad:
        continue
    print(f'{line}  {stack}')
    # It's an incomplete line
    for i in range(len(stack)-1,-1,-1):
        c = stack[i]
        lineAns *= 5
        lineAns += points[c]
    scores.append(lineAns)

print(scores)

scores.sort()
index = len(scores) // 2
print(scores[index])