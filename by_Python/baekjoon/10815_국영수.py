import sys
from collections import namedtuple
input = sys.stdin.readline

n = int(input())
Student = namedtuple('Student', ['name', 'korean', 'english', 'math'])
arr = []
for _ in range(n):
    tmp = input().split()
    arr.append(Student(tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])))

arr.sort(key = lambda x : (-x.korean, x.english, -x.math, x.name))
for x in arr:
    print(x.name)