import sys
input = sys.stdin.readline

S = input().strip()
ans = ""

tag = False
stack = []

for i in range(len(S)):
    if S[i] == '<':
        while stack:
            ans += stack.pop()
        ans += S[i]
        tag = True

    elif S[i] == '>':
        ans += S[i]
        tag = False

    elif S[i] == ' ':
        while stack:
            ans += stack.pop()
        ans += S[i]

    else:
        if tag:
            ans += S[i]
        else:
            stack.append(S[i])

# 아직 스택에 문자가 존재하면
while stack:
    ans += stack.pop()

print(ans)
