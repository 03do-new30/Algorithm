import sys
input = sys.stdin.readline

"""
이친수는 0으로 시작하지 않는다.
이친수에서는 1이 두 번 연속으로 나타나지 않는다.
(11을 부분 문자열로 갖지 않는다)
"""
n = int(input().strip())
pinary = [0 for i in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        pinary[1] = 1
    elif i == 2:
        pinary[2] = 1
    else:
        pinary[i] = pinary[i-2] + pinary[i-1]
print(max(pinary))
