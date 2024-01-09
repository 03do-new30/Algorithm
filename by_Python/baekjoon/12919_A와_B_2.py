import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

"""
T를 기준으로 첫글자와 끝글자로 판단한다
A___B : 아무 행동도 할 수 없음
A___A : 문자열 끝의 A 삭제
B___A : 문자열 끝의 A 삭제 혹은 문자열을 뒤집고 문자열 끝의 B 삭제
B___B : 문자열을 뒤집고 끝의 B 삭제
"""
def solve(string, goal):
    # print("string:", string)
    if len(string) == len(goal):
        # print("## string:", string, "goal:", goal)
        if string == goal:
            return 1
        return 0
    if string[0] == 'A':
        if string[-1] == 'A':
            # 문자열 끝의 A 삭제
            return solve(string[:-1], goal)
        else:
            if string == goal:
                return 1
            else:
                return 0
    else:
        if string[-1] == 'A':
            # 문자열 끝의 A 삭제
            x = solve(string[:-1], goal)
            if x == 1:
                return 1
            # 문자열을 뒤집고 문자열 끝의 B 삭제
            x = solve(string[::-1][:-1], goal)
            if x == 1:
                return 1
        else:
            # 문자열을 뒤집고 문자열 끝의 B 삭제
            return solve(string[::-1][:-1], goal)
    return 0

ans = solve(t, s)
print(ans)