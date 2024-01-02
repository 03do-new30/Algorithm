import sys
input = sys.stdin.readline

# 출발 후, 막다른 점까지 도착할 때까지 가장 많이 방문할 수 있는 칸
# 케이스 나눠야 함

"""
1. height = 1인 경우
- 움직일 수 없으므로 정답은 1

2. height = 2인 경우
- 두가지 방법만 사용 가능 (2번 방법, 3번 방법)
- 정답은 min(4, (width + 1) / 2) -> 최소 이동 횟수 제한

3. height >= 3인 경우
3-1. width >= 7
    - 4가지 방법을 모두 사용하면 (7, 1)로 이동한다
    - 여기서부터 1번과 4번 방법을 번갈아가면서 사용하면 매 넓이마다 방문 가능
    - width -2 (2번 방법과 3번 방법을 이용했을 때 방문하지 못한 2칸)
3-2. width < 7
    - 4가지 방법을 모두 사용할 수 없다
    - 1번과 4번 방법을 번갈아가면서 사용할 수 있다
    - min(4, width)
"""

height, width = map(int, input().split())

if height == 1:
    print(1)
elif height == 2:
    print(min(4, (width + 1) // 2))
else:
    if width < 7:
        print(min(4, width))
    else:
        print(width - 2)