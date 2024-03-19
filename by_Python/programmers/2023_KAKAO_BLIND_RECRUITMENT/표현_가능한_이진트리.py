from math import log

def solve(binary):
    if len(binary) == 1:
        return True
    
    left = 0
    right = len(binary) - 1
    mid = (left + right) // 2

    if binary[mid] == '0':
        # 현재 탐색중인 서브트리의 루트노드가 더미인 경우
        # 그 아래 노드들이 모두 0이어야 한다
        left_tree = binary[:mid]
        right_tree = binary[mid + 1:]
        if '1' not in left_tree and '1' not in right_tree:
            return True
        else:
            return False
    # 현재 탐색중인 서브트리의 루트노드가 더미가 아닌 경우
    left_tree = binary[:mid]
    right_tree = binary[mid + 1:]
    return solve(left_tree) and solve(right_tree)
    

def solution(numbers):
    binarys = [] # 숫자를 이진수로 변환한 문자열을 저장
    for num in numbers:
        binarys.append(bin(num)[2:])
    
    for i in range(len(binarys)):
        # 포화 이진트리의 노드 개수는 2^n - 1
        # 2^n - 1개의 노드를 가질 수 있게 좌측에 0을 붙여준다
        while log(len(binarys[i]) + 1, 2) % 1 != 0:
            binarys[i] = '0' + binarys[i]
           
    result = []
    for binary in binarys:
        ret = solve(binary)
        if ret:
            result.append(1)
        else:
            result.append(0)
    return result



numbers = [[7, 42, 5], [63, 111, 95], [423, 15]]
result = [[1, 1, 0], [1, 1, 0], [0, 1]]

for i in range(len(numbers)):
   print('결과:', solution(numbers[i]) == result[i])
   print('-' * 40)