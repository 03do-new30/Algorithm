from collections import deque
import sys
input = sys.stdin.readline

# d-dzdzdz=dz
string = input().strip()

# 3글자짜리 "dz="가 "z="보다 먼저 replace될 수 있게 앞에 배치
alphabet = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for x in alphabet:
    string = string.replace(x, "*")
    # print(x, "-> *:", string)

print(len(string))
