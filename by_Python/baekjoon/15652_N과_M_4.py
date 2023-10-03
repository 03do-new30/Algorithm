import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = [0] * (n+1)  # cnt[i] = 숫자 i가 몇번 등장하는지 저장

# num - 포함할지 말지 결정해야 할 숫자
# selected - 현재까지 선택한 수의 개수


def solve(num, selected):  # 선택의 관점
    if selected == m:
        # cnt에 저장된 등장 횟수를 이용하여 출력한다
        seq = []
        for i in range(1, n+1):
            for j in range(cnt[i]):
                seq.append(str(i))
        print(' '.join(seq))
        return

    if num > n:
        return

    # 선택하는 경우
    # 몇 개를 중복으로 선택할건지
    for i in range(m-selected, 0, -1):  # 사전순으로 출력하기 위한 순서
        cnt[num] = i
        solve(num + 1, selected + i)
    # 선택하지 않는 경우
    cnt[num] = 0
    solve(num + 1, selected)


solve(1, 0)
