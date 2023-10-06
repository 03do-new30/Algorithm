import sys
input = sys.stdin.readline

# 순열을 구한 뒤
# 최소 비용 계산
# N * N!
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    # seq[i-1]보다 크면서 seq[i:] 에서 가장 작은 수
    while seq[i-1] >= seq[j]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]

    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    
    return True


def calc(seq):
    ret = 0
    for i in range(len(seq)):
        if i == len(seq) - 1:
            if arr[seq[i]][seq[0]] == 0:
                return -1
            ret += arr[seq[i]][seq[0]] # 마지막 도시에서 원점으로 돌아가는 경우
        else:
            if arr[seq[i]][seq[i+1]] == 0:
                return -1
            ret += arr[seq[i]][seq[i+1]]
    return ret



a = [x for x in range(n)] # 첫 순열
min_cost = 10000000
while True:
    ret = calc(a)
    if ret != -1:
        min_cost = min(min_cost, ret)
    if not next_permutation(a):
        break
print(min_cost)
