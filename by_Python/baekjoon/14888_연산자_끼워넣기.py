import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
signs = list(map(int, input().split())) # +, -, *, //

min_result = 10000000000
max_result = -10000000000

# 순열로 풀어보기
# 연산자 -> 순열로 만든다
seq = [0] * signs[0] + [1] * signs[1] + [2] * signs[2] + [3] * signs[3]
def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    while seq[i-1] >= seq[j]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]

    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    
    return True

while True:
    result = a[0]
    for i in range(n-1):
        if seq[i] == 0: # +
            result += a[i+1]
        elif seq[i] == 1: # -
            result -= a[i+1]
        elif seq[i] == 2: # *
            result *= a[i+1]
        else: # /
            if result < 0:
                result = -(-result // a[i+1])
            else:
                result //= a[i+1]
    min_result = min(min_result, result)
    max_result = max(max_result, result)
    if not next_permutation(seq):
        break

print(max_result)
print(min_result)
