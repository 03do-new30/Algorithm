import sys
input = sys.stdin.readline

binary = input().strip()

while len(binary) % 3 != 0:
    binary = '0' + binary

answer = ''
for i in range(0, len(binary)-2, 3):
    answer += str(int(binary[i:i+3], 2))
print(answer)