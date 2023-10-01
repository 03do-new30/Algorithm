import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m > 0:
    broken = list(map(int, input().split()))
    btns = [] # 고장나지 않은 버튼 저장
    for i in range(10):
        if i not in broken:
            btns.append(i)
else:
    btns = [i for i in range(10)]

chnl = 100
cnt = 0
ans = 0

### 1 ###
# (+), (-)만으로 이동하는 경우 입력 횟수
plus_minus = abs(n - chnl)
ans = plus_minus

if ans == 0:
    print(ans)
    exit()

### 2 ###
# 고장나지 않은 버튼으로 주어진 채널 자릿수 숫자를 만들 수 있는 모든 경우
# 최대 6자리까지 존재할 수 있음
# 최대 10^6회의 연산이므로 2초 안에 실행 가능함
for a in btns:
    tmp_a = str(a)
    ans = min(ans, 1 + abs(n - int(tmp_a)))
    # 1 + abs(n - int(tmp_a)) = 숫자버튼 누른 횟수 + n이 되기 위해 (+), (-) 조정 횟수

    if tmp_a == str(n):
        break

    for b in btns:
        tmp_b = tmp_a + str(b)
        ans = min(ans, 2 + abs(n - int(tmp_b)))
        if tmp_b == str(n):
            break

        for c in btns:
            tmp_c = tmp_b + str(c)
            ans = min(ans, 3 + abs(n - int(tmp_c)))
            if tmp_c == str(n):
                break

            for d in btns:
                tmp_d = tmp_c + str(d)
                ans = min(ans, 4 + abs(n - int(tmp_d)))
                if tmp_d == str(n):
                    break

                for e in btns:
                    tmp_e = tmp_d + str(e)
                    ans = min(ans, 5 + abs(n - int(tmp_e)))
                    if tmp_e == str(n):
                        break

                    for f in btns:
                        tmp_f = tmp_e + str(f)
                        ans = min(ans, 6 + abs(n - int(tmp_f)))
                        if tmp_f == str(n):
                            break

print(ans)