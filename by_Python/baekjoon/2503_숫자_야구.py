import sys
input = sys.stdin.readline
from itertools import permutations

perms = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(int(input())):
    ask, strike, ball = input().split()
    strike = int(strike)
    ball = int(ball)

    be_removed = [] # 지워질 순열들
    for perm in perms:
        # 어떤 순열 perm이 strike, ball의 값을 만족하지 않으면 지워짐
        s = b = 0
        for i in range(3):
            if int(ask[i]) == perm[i]:
                s += 1
            else:
                if int(ask[i]) in perm:
                    b += 1
        
        if strike != s or ball != b:
            be_removed.append(perm)
    
    # 지워질 순열 삭제
    for perm in be_removed:
        perms.remove(perm)
    
print(len(perms))