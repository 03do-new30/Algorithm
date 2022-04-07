import sys
input = sys.stdin.readline

T = int(input())
count = [0, 0, 0]
impossible = False
while T > 0:
    if T >= 300:
        T-= 300
        count[0] += 1
    elif T >= 60:
        T -= 60
        count[1] += 1
    elif T >= 10:
        T -= 10
        count[2] += 1
    else:
        impossible = True
        break

if impossible:
    print(-1)
else:
    print(' '.join(map(str, count)))
    