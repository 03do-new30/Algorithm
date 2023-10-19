import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

# 등장한 알파벳 개수가 k라면
# 0-9 중 가장 큰 수 k개를 고른다
# 브루트포스로 알파벳과 매칭해 가장 큰 합이 나오는 결과를 고른다

### 1 ### 
# 등장한 알파벳 개수 k에 저장
alpahbets = set()
for word in words:
    tmp = set(word)
    alpahbets = alpahbets.union(tmp)
k = len(alpahbets)

# 0-9 중 가장 큰 수 k개를 고른다
nums = [x for x in range(9, 9-k, -1)]

# 알파벳과 매칭해서 가장 큰 합이 나오는 결과를 고른다
# 알파벳과 매칭하는 방법
# 알파벳에 1:1로 대응되는 인덱스를 부여한다
# 큰 수를 순열로 쭉 만들어보고, 순열의 인덱스와 알파벳의 인덱스가 같은 것들을 매칭
alpahbets = sorted(list(alpahbets))

# nums를 순열로 만든다
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
    word_num_dict = dict()
    for i in range(k):
        w = alpahbets[i]
        n = nums[i]
        word_num_dict[w] = n
    
    sum = 0
    for word in words:
        if len(word) == 1:
            sum += int(str(word_num_dict[word]))
            continue
        result = ''
        for x in word:
            result += str(word_num_dict[x])
        sum += int(result)
    
    answer = max(answer, sum)

    if not prev_permutation(nums):
        break

print(answer)