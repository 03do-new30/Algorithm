import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit()

answer = ''
while n != 0:
    r = n % - 2
    if r == -1:
        answer = '1' + answer
        n = n // -2 + 1
    else:
        answer = str(r) + answer
        n = n // -2
print(answer)