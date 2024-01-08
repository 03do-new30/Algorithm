import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

# t를 s로 만들 수 있는지 주어진 연산을 거꾸로 수행하며 확인
while len(s) != len(t):
    # t의 마지막 문자가 A인 경우 A를 뺀다
    if t[-1] == 'A':
        t = t[:-1]
        continue
    # t의 마지막 문자가 B인 경우 B를 빼고 문자열을 뒤집는다
    if t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
        continue

if s == t:
    print(1)
else:
    print(0)
