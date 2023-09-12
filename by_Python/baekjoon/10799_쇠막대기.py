import sys
input = sys.stdin.readline

string = input().strip()

answer = 0
tmp = 0
for i in range(len(string)):
    if string[i] == '(':
        tmp += 1
    else:
        tmp -= 1
        if string[i-1] == '(':
            answer += tmp
        else:
            answer += 1
print(answer)