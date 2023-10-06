import sys
input = sys.stdin.readline

def prev_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] <= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    while seq[i-1] <= seq[j]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]

    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

n = int(input())
seq = list(map(int, input().split()))
if prev_permutation(seq):
    print(' '.join(list(map(str, seq))))
else:
    print(-1)