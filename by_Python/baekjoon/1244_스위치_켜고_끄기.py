import sys
input = sys.stdin.readline

def boy(num):
    idx = num
    while idx <= n:
        swch[idx] = 0 if swch[idx] == 1 else 1
        idx += num

def girl(num):
    i = 0
    while 1 <= num - i and num + i <= n:
        if swch[num-i] != swch[num+i]:
            break

        x = swch[num-i]
        swch[num-i] = swch[num+i] = 0 if x == 1 else 1

        i += 1

n = int(input())
swch = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    sex, num = map(int, input().split())
    if sex == 1:
        boy(num)
    else:
        girl(num)

# 스위치의 상태를 한 줄에 20개씩 출력한다.
for i in range(1, n+1):
    if i % 20 == 0:
        print(swch[i])
    else:
        print(swch[i], end = ' ')