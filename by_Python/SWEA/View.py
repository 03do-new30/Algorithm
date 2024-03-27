import sys
sys.stdin = open("by_Python/SWEA/inputs/View.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    # view[i] = i번째 건물에서 조망권이 확보된 세대 수
    view = [0] * n

    for i in range(2, n-2):
        left_view = buildings[i] - max(buildings[i-2], buildings[i-1])
        right_view = buildings[i] - max(buildings[i+1], buildings[i+2])
        
        view[i] = min((left_view if left_view > 0 else 0), (right_view if right_view > 0 else 0))
    
    print("#{0} {1}".format(test_case, sum(view)))