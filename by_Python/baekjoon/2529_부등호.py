import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

visited = [False] * 10
answers = []
def solve(idx, seq):
    # 성공
    # print("idx:", idx, "seq:", seq)
    if idx == k:
        answers.append(seq)
        return seq

    if signs[idx] == '<':
        for i in range(10):
            if seq[idx] < i and not visited[i]:
                visited[i] = True
                solve(idx + 1, seq + [i])
                visited[i] = False
    else:
        for i in range(10):
            if seq[idx] > i and not visited[i]:
                visited[i] = True
                solve(idx + 1, seq + [i])
                visited[i] = False

for i in range(10):
    visited[i] = True
    solve(0, [i])
    visited[i] = False

print(''.join(list(map(str, answers[-1]))))
print(''.join(list(map(str, answers[0]))))