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

# 재귀로 풀어보기
def solve(idx, password):
    if len(password) == ll:
        if is_password(password):
            print(password)
        return
    
    if idx >= c:
        return
    
    # idx번째 알파벳을 암호에 포함
    solve(idx + 1, password + letters[idx])
    # idx번째 알파벳을 암호에 미포함
    solve(idx + 1, password)

solve(0, "")