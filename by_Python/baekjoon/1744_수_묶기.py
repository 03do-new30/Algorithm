import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

# 양수는 양수끼리, 음수는 음수끼리 묶자
# 양수 -> 가장 큰수 두개 and 음수 -> 가장 작은 수 두개
# 1은 묶지 않는 것이 좋다
# 0은 음수를 지울 수 있다 -> 묶이지 않는 음수가 있는 경우 0을 이용할 수 있다
pos = [] # 양수
neg = [] # 음수
zeros = 0 # 0의 개수
for x in a:
    if x > 0:
        pos.append(x)
    elif x < 0:
        neg.append(x)
    else:
        zeros += 1

ans = 0

pos_check = [False] * len(pos)
pos.sort(reverse = True)
for i in range(len(pos)):
    if pos_check[i]:
        continue
    if i+1 < len(pos) and pos[i] * pos[i+1] > pos[i] + pos[i+1]:
        pos_check[i] = pos_check[i+1] = True
        ans += pos[i] * pos[i+1]
        continue
    ans += pos[i]
    pos_check[i] = True
# print("pos_check:", pos_check)
# print("ans:", ans)

neg_check = [False] * len(neg)
neg.sort()
for i in range(len(neg)):
    if neg_check[i]:
        continue
    if i + 1 < len(neg) and neg[i] * neg[i+1] > neg[i] + neg[i+1]:
        neg_check[i] = neg_check[i+1] = True
        ans += neg[i] * neg[i+1]
        continue
# print("neg_check:", neg_check)
# print("ans:", ans)

# 남은 neg 처리
# print("zeros:", zeros)
for i in range(len(neg)):
    if not neg_check[i] and zeros > 0:
        neg_check[i] = True
        zeros -= 1
for i in range(len(neg)):
    if not neg_check[i]:
        ans += neg[i]
# print("neg_check:", neg_check)
# print("ans:", ans)
print(ans)