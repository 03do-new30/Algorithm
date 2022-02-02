import sys
input = sys.stdin.readline

hexa = input().strip()
n = len(hexa)-1

ans = 0
for x in hexa:
    if x.isalpha():
        ans += (ord(x)-65+10) * 16**n
    else:
        ans += int(x) * 16**n
    n -= 1

print(ans)
