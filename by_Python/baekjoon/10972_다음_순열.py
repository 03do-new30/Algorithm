import sys
input = sys.stdin.readline

def next_permutation(seq):
    ### 1 ###
    # seq[i-1] < seq[i]를 만족하는 가장 큰 i를 찾는다
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i == 0:
        return False
    ### 2 ### 
    # seq[i-1] < seq[j]를 만족하는 가장 작은 seq[j]를 찾고, 위치를 바꾼다 (i <= j < n)
    j = len(seq) - 1
    while seq[j] <= seq[i-1]:
        j -= 1
    
    seq[i-1], seq[j] = seq[j], seq[i-1]
    
    ### 3 ###
    # seq[:i] + reversed(seq[i:])를 하면 seq[:i]로 시작하는 순열중 가장 첫번째 순열이 완성된다
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        j -= 1
        i += 1
    return True

n = int(input())
seq = list(map(int, input().split()))

success = next_permutation(seq)
if not success:
    print(-1)
else:
    print(' '.join(list(map(str, seq))))