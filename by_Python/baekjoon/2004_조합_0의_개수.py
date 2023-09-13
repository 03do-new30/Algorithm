import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

cnt2 = 0
cnt5 = 0

def get_cnt(x, prime):
    ret = 0
    saved_prime = prime
    while x >= prime:
        ret += x // prime
        prime *= saved_prime
    return ret

cnt2 = get_cnt(n, 2) - get_cnt(n-m, 2) - get_cnt(m, 2)
cnt5 = get_cnt(n, 5) - get_cnt(n-m, 5) - get_cnt(m, 5)
print(min(cnt2, cnt5))