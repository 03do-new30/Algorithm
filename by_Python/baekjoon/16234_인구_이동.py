from collections import deque
import sys
input = sys.stdin.readline

""" 입력 """
N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]


def solve():
    ans = 0

    while True:
        """
        (r1, c1), (r2, c2)가 국경선을 공유할 수 있다면
        border[r1][c1] == border[r2][c2], 같은 코드를 가짐
        """
        border = [[0]*N for _ in range(N)]
        code = 1
        for r in range(N):
            for c in range(N):
                if border[r][c] == 0:
                    bfs(r, c, border, code)
                    code += 1

        """ bfs 수행 후 border 출력하는 코드
        print("bfs 이후 border 상태")
        for border_row in border:
            print(border_row)
        """

        """
        union_info
        union_info[code] = [(r1, c1), (r2, c2), ...]
        같은 code를 공유하는 연합국들의 좌표를 저장한다
        """
        union_info = [[] for _ in range(code)]
        for r in range(N):
            for c in range(N):
                if border[r][c] != 0:
                    union_info[border[r][c]].append((r, c))

        """ union_info 출력하는 코드
        print("union_info")
        for union_info_row in union_info:
            print(union_info_row)
        """

        # 인구 이동 시키기
        stop = True
        for i in range(1, code):
            # 한 국가만 있는 연합은 연합이 아니다
            if len(union_info[i]) <= 1:
                continue
            else:
                stop = False  # 연합이 하나라도 존재하면 stop 하지 않는다

                union_count = len(union_info[i])  # 연합을 이루는 칸의 개수
                union_people = 0  # 연합의 인구 수
                for x in union_info[i]:
                    union_people += country[x[0]][x[1]]
                union_people = union_people // union_count  # 인구 수

                # 인구를 이동시킨다
                for x in union_info[i]:
                    country[x[0]][x[1]] = union_people

        if stop:
            return ans  # 더이상 이동 없음. loop 종료, 함수 반환
        else:
            ans += 1  # 날짜 카운트 증가

    return ans


def bfs(r, c, border, code):
    q = deque([(r, c)])
    border[r][c] = code
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        r, c = q.popleft()
        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]
            if 0 <= new_r < N and 0 <= new_c < N:
                if border[new_r][new_c] == 0:
                    # 인구 차이
                    diff = abs(country[r][c] - country[new_r][new_c])
                    if L <= diff <= R:
                        # 국경선을 공유
                        border[new_r][new_c] = border[r][c]
                        q.append((new_r, new_c))


print(solve())
