import sys
input = sys.stdin.readline

from collections import deque

def solve_bfs(n, m, k):

    # visited에 (만들어진 수, 교환연산 횟수)를 저장한다.
    visited = set()
    visited.add((n, 0))
    q = deque([(n, 0)])

    answer = 0

    while q:
        n, cnt = q.popleft()
        if cnt == k:
            answer = max(answer, n)
            continue
        
        n_list = list(str(n))
        for i in range(m-1):
            for j in range(i+1, m):
                if i == 0 and n_list[j] == '0':
                    continue
                
                # 교환 연산으로 new_n을 만들어주는 과정
                n_list[i], n_list[j] = n_list[j], n_list[i]
                new_n = int(''.join(n_list))

                if (new_n, cnt + 1) not in visited:
                    q.append((new_n, cnt + 1))
                    visited.add((new_n, cnt  + 1))
                
                # 교환 연산 원복
                n_list[i], n_list[j] = n_list[j], n_list[i]

    return answer if answer else -1

# main
n, k = input().split()

m = len(n)
n = int(n)
k = int(k)

print(solve_bfs(n, m, k))