import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

# 부등호 관계를 만족하는 최대정수, 최소정수
# 최대정수 = 주어진 숫자 중 가장 큰 숫자 (k+1)개로 만든 순열
# 최소정수 = 주어진 숫자 중 가장 작은 숫자 (k+1)개로 만든 순열
# 위 중 부등호 관계를 만족하는 것을 출력하면 된다!

bigs =[x for x in range(9, 8-k, -1)] # 큰 수 (k+1)개
smalls = [x for x in range(0, k+1)] # 작은 수 (k+1)개

# 순열이 부등호 관계를 만족하는지 체크
def check(seq):
    for i in range(k):
        if signs[i] == '<':
            if seq[i] < seq[i+1]:
                continue
            else:
                return False
        else:
            if seq[i] > seq[i+1]:
                continue
            else:
                return False
    return True

def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    while seq[j] <= seq[i-1]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]
    
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

def prev_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] <= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    while seq[j] >= seq[i-1]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]
    
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

# 큰 수는 prev_permutation으로 가면서 부등호 관계를 체크해보기
while not check(bigs):
    prev_permutation(bigs)
print(''.join(list(map(str, bigs))))
# 작은 수는 next_permutation으로 가면서 부등호 관계를 체크해보기
while not check(smalls):
    next_permutation(smalls)
print(''.join(list(map(str, smalls))))