import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
# E S M으로 표시되는 가장 빠른 연도를 출력한다

# 1 2 3 -> 5266

year = 1
while True:
    E_success = False
    S_success = False
    M_success = False

    if year % 15 == 0:
        if E == 15:
            E_success = True
    else:
        if E == year % 15:
            E_success = True

    if year % 28 == 0:
        if S == 28:
            S_success = True
    else:
        if S == year % 28:
            S_success = True

    if year % 19 == 0:
        if M == 19:
            M_success = True
    else:
        if M == year % 19:
            M_success = True

    if S_success and E_success and M_success:
        print(year)
        break

    year += 1
