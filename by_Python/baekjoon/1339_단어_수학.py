import sys
input = sys.stdin.readline

n = int(input())
words = []
letters = []
for _ in range(n):
    word = input().strip()
    words.append(word)
    for x in word:
        letters.append(x)
letters = list(set(letters)) # 등장하는 알파벳 저장

### 1 ###
# 등장한 알파벳 개수 k에 저장
k = len(letters)

# 0-9 중 가장 큰 수 k개를 고르고, 순열로 만든 뒤 알파벳과 매칭
nums = [x for x in range(9, 9-k, -1)]

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

answer = 0

while True:
    matches = dict()
    for i in range(k):
        ll = letters[i]
        nn = nums[i]
        matches[ll] = nn
    
    tmp = 0
    for word in words:
        word_num = ''
        for x in word:
            word_num += str(matches[x])
        word_num = int(word_num)
        tmp += word_num
    
    answer = max(answer, tmp)

    if not prev_permutation(nums):
        break

print(answer)
