# 서로 다른 L개의 알파벳 소문자들
# 최소 한 개의 모음과 최소 두 개의 자음으로 구성된다
# 암호는 알파벳이 증가하는 순서로 배열되엇다

# C개의 문자들.. 가능성 있는지 판별하라
# C개의 문자로 암호를 만든다면
# 암호인지 아닌지 판별하는 시간만 해도
# 최대 15개의 문자들 중 L가지를 고른다

import sys
input = sys.stdin.readline

ll, c = map(int, input().split())
letters = input().split()
letters.sort() #사전순 정렬

# 암호 판별
def is_password(a):
    # 최소 한개의 모음과 두개의 자음인가?
    vowel_count = 0
    for vowel in 'aeiou':
        vowel_count += a.count(vowel)
    
    consonant_count = len(a) - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        return True
    return False

# 다음 순열
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


# 6603 로또 문제와 비슷하게 풀어보기
seq = [0] * (c - ll) + [1] * ll
permutations = []
while True:
    permutations.append(seq[:])
    if not next_permutation(seq):
        break

permutations.sort(reverse=True)
for permutation in permutations:
    password = []
    for i in range(c):
        if permutation[i] == 1:
            password.append(letters[i])
    if is_password(password):
        print(''.join(password))
