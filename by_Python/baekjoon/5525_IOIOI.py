# 출처: https://black-hair.tistory.com/135
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

idx, count = 0, 0
answer = 0

while idx < M - 1:
    if S[idx:idx+3] == 'IOI':
        idx += 2 # 다음 IOI를 찾는다. IOI(OI)(OI)
        count += 1

        if count == N:
            answer += 1
            count -= 1 # 겹치는 게 있을 수 있다.
    
    else:
        idx += 1 # idx+1을 시작점으로 다시 IOI를 찾는다.
        count = 0

print(answer)