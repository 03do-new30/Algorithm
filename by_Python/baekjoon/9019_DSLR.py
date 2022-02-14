import sys
input = sys.stdin.readline


def solve(A, B):
    # (현재 A값, 지금까지 수행한 연산)을 q에 삽입
    q = deque([(A, "")])
    visited[A] = True

    while q:
        A, dslr = q.popleft()

        if A == B:
            print(dslr)
            break

        # D
        new_A = A * 2 % 10000

        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, dslr + "D"))

        # S
        if A == 0:
            new_A = 9999
        else:
            new_A = A - 1

        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, dslr + "S"))

        # L
        new_A = (A % 1000) * 10 + A // 1000
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, dslr + "L"))

        # R
        new_A = (A % 10)*1000 + (A//10)
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, dslr + "R"))


T = int(input().strip())
for _ in range(T):
    # 연산 횟수를 줄이기 위해,
    # A값이 i일 때 DSLR 연산을 시도해보았다면
    # vsited[i] = True
    visited = [False]*100000
    A, B = map(int, input().split())
    solve(A, B)
