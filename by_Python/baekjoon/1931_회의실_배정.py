import sys
input = sys.stdin.readline

n = int(input())
# "빨리 끝나는" 회의부터 배정 -> 그래야 뒤에 배정할 회의가 더 많음
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# end를 기준으로 정렬
meetings.sort(key=lambda x : (x[1], x[0]))
ans = 0

last_time = 0 # 가장 마지막에 끝난 회의 시간 저장
for meeting in meetings:
    start, end = meeting
    if start >= last_time:
        last_time = end
        ans += 1
print(ans)