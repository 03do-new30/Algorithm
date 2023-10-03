import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = [-1] * (m+1)  # 수열 저장
visited = [False] * (n+1)


def solve(idx):
    if idx == m+1:  # 수열의 길이가 m이 되면 출력
        print(' '.join(list(map(str, seq[1:]))))
        return

    # idx번째에 수를 추가
    for num in range(1, n+1):
        if visited[num]:
            continue
        seq[idx] = num
        visited[num] = True
        solve(idx + 1)
        visited[num] = False


visited[0] = True
solve(1)
