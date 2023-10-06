import sys
input = sys.stdin.readline

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    return True

def calc(a):
    ret = 0
    for i in range(1, len(a)):
        ret += abs(a[i] - a[i-1])
    return ret

n = int(input())
a = list(map(int, input().split()))
a.sort()

# 주어진 정수들로 순열을 만들어보며 하나하나 최댓값 구함
# N! = 8! = 40320
# N * N!
answer = -100
while True:
    answer = max(answer, calc(a))
    if not next_permutation(a):
        break
print(answer)