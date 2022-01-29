import sys
input = sys.stdin.readline

# 저작권이 있는 멜로디의 평균값
# 저작권이 있는 멜로디의 개수 / 앨범에 수록된 곡의 개수 -> 항상 올림해서 정수로

# a = 앨범에 수록된 곡의 개수,
# i = 평균값
a, i = map(int, input().split())
print(i*a - a + 1)
