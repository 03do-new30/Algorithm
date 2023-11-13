import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# words[i] = i번쨰 단어를 구성하고 있는 알파벳을 비트마스크로 저장
words = [0] * n
for i in range(n):
    word = list(set(list(input().strip())))
    for x in word:
        words[i] = words[i] | 1 << (ord(x) - 97)

def solve(idx, k, mask):
    if k < 0:
        return 0
    
    if idx == 26:
        return count(mask, words)
    
    ans = 0
    
    tmp1 = solve(idx + 1, k - 1, mask | (1 << idx)) # idx번쨰 알파벳을 배우는 경우
    
    ans = max(ans, tmp1)

    # idx번째 알파벳을 배우지 않는 경우
    if idx not in [ord(x) - 97 for x in 'antic']:
        tmp2 = solve(idx + 1, k, mask)
        ans = max(ans, tmp2)
    
    return ans

def count(mask, words):
    cnt = 0
    for word in words:
        if word & ((1 << 26) - 1 - mask) == 0:
            cnt += 1
    return cnt

answer = solve(0, k, 0)
print(answer)
