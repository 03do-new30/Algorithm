import sys
input = sys.stdin.readline

# 다음 순열로 구한다
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

while True:
    tc = list(map(int, input().split()))
    k = tc[0]
    if k == 0:
        break
    nums = tc[1:]

    # 여섯개의 수를 고르는 방법은
    # '1' 6개와 '0' (k-6)개 로 만들 수 있는 모든 순열을 통해 구할 수 있다
    # 1 -> 숫자를 고르는 경우
    # 0 -> 숫자를 고르지 않는 경우
    seq = [0] * (k-6) + [1] * (6)
    
    answer = []
    while True:
        answer.append(seq[:])
        if not next_permutation(seq):
            break
    
    answer.sort(reverse=True)
    
    for ans in answer:
        tmp = []
        for i in range(k):
            if ans[i] == 1:
                tmp.append(nums[i])
        print(' '.join(map(str, tmp)))

    print()