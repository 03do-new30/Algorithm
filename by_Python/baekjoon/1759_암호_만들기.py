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
