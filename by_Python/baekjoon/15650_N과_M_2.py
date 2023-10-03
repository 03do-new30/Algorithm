import sys
input = sys.stdin.readline

n, m = map(int, input().split())

seq = [-1] * m  # 수열 저장

# "선택" 의 관점에서 진행
# (4, 1, 7)을 선택했을 때 나오는 오름차순 수열은 단 하나 -> 1, 4, 7
# 선택할지 말지만 검사해도 풀이 가능 O(2^n)

###########################################
# num -> 선택할지 말지 결정할 수
# selected -> 현재까지 선택한 수의 개수
###########################################


def solve(num, selected):
    if selected == m:
        print(' '.join(list(map(str, seq))))
        return

    if num > n:
        return

    # num을 선택하는 경우
    seq[selected] = num
    solve(num + 1, selected + 1)
    # num을 선택하지 않는 경우
    seq[selected] = -1
    solve(num + 1, selected)


solve(1, 0)
