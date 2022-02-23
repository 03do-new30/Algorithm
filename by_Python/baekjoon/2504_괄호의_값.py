import sys
input = sys.stdin.readline


def is_correct(string):
    # 올바른 괄호열인지 체크
    stack = []
    for x in string:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) > 0:
                popped = stack.pop()
                if popped != '(':
                    return False
            else:
                return False
        elif x == '[':
            stack.append(x)
        elif x == ']':
            if len(stack) > 0:
                popped = stack.pop()
                if popped != '[':
                    return False
            else:
                return False

    if len(stack) > 0:
        return False

    return True


def find_pair_idx(string):
    # idx0에 왼쪽 괄호가 위치할 때, 그 짝이 되는 오른쪽 괄호의 idx를 찾는다
    stack = []
    for idx in range(len(string)):
        if string[idx] == '(' or string[idx] == '[':
            stack.append(string[idx])
        elif string[idx] == ')' or string[idx] == ']':
            stack.pop()

        # stack 비었는지 확인
        if len(stack) == 0:
            return idx

    return -1


def solve(string):
    ans = 0

    if string == "":
        return ans

    if string[0] == '(':
        if string[1] == ')':
            ans += 2 + solve(string[2:])
        else:
            pair_idx = find_pair_idx(string)
            ans += 2 * solve(string[1:pair_idx]) + solve(string[pair_idx+1:])

    elif string[0] == '[':
        if string[1] == ']':
            ans += 3 + solve(string[2:])
        else:
            pair_idx = find_pair_idx(string)
            ans += 3 * solve(string[1:pair_idx]) + solve(string[pair_idx+1:])

    return ans


string = input().strip()
if is_correct(string):
    print(solve(string))
else:
    print(0)
