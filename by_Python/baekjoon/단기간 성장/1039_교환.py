import sys
input = sys.stdin.readline

def solve(n, m, k):
    # 한자리수이면 연산을 수행할 수 없다.
    if m == 1:
        return -1

    # n으로 만들 수 있는 최대 정수
    max_n = sorted(n, reverse=True)

    # 최대 정수에서, 숫자가 연속되는 부분이 있다면
    # k번째 연산에 도달하기 전 max_n을 만들 수 있는 경우 그 다음 연산들은 모두 max_n의 결과를 낼 수 있다.
    has_continuous_number = False
    for i in range(m-1):
        if max_n[i] == max_n[i+1]:
            has_continuous_number = True
            break

    # k_result[i] = 연산을 i번 했을 때 만들어지는 최대 정수(리스트로 저장)
    k_result = [[] for _ in range(k+1)]
    k_result[0] = n

    for i in range(1, k+1):
        
        prev = k_result[i-1] # 이전 연산에서 만들어진 최대 정수

        if prev == max_n:
            if has_continuous_number:
                k_result[i] = prev
            else:
                # 끝의 두 수를 swap
                new_n = prev[:]
                new_n[m-1], new_n[m-2] = new_n[m-2], new_n[m-1]
                k_result[i] = new_n
        
        else:
            swapped = False # 연산을 수행했는지 여부

            for j in range(m):
                
                if swapped:
                    break
                if max_n[j] != prev[j]:
                    # max_n[j]가 prev에서 몇번째 인덱스에 위치하는지 찾는다. 이때, max_n[j]가 여러개 있다면 가장 뒤에 있는 인덱스를 반환한다.
                    index = m - 1 - prev[::-1].index(max_n[j])
                    
                    # prev의 j와 index를 swap한다.
                    new_n = prev[:]
                    new_n[j], new_n[index] = new_n[index], new_n[j]

                    swapped = True
                    k_result[i] = new_n
        
        # 0이 앞자리에 오는지 확인한다.
        if k_result[i][0] == 0:
            return -1
    print(max_n, "\nk_result", k_result)
    return ''.join(list(map(str, k_result[k])))


def new_solve(n, m, k):
    # 한자리수이면 연산을 수행할 수 없다.
    if m == 1:
        return -1
    
    # n으로 만들 수 있는 최대 정수
    max_n = sorted(n, reverse=True)

    # 최대 정수에서, 숫자가 연속되는 부분이 있다면
    # k번째 연산에 도달하기 전 max_n을 만들 수 있는 경우 그 다음 연산들은 모두 max_n의 결과를 낼 수 있다.
    has_continuous_number = False
    for i in range(m-1):
        if max_n[i] == max_n[i+1]:
            has_continuous_number = True
            break

    # k_result[i] = 연산을 i번 했을 때 만들어지는 최대 정수(리스트로 저장)
    k_result = [[] for _ in range(k+1)]
    k_result[0] = n

    return dfs(k_result, 1, max_n, has_continuous_number)

def get_index_list(target_list, target_num):
    ret = []
    for i in range(len(target_list)):
        if target_list[i] == target_num:
            ret.append(i)
    return ret

def dfs(k_result, i, max_n, has_continuous_number):
    prev = k_result[i-1] # 이전 연산에서 만들어진 최대 정수
    
    ret = 0

    # 0이 앞자리에 오는지 확인한다.
    if prev[0] == 0:
        return -1
    
    if i == k+1:
        return int(''.join(list(map(str, k_result[k]))))

    if prev == max_n:
        if has_continuous_number:
            k_result[i] = prev
        else:
            # 끝의 두 수를 swap
            new_n = prev[:]
            new_n[m-1], new_n[m-2] = new_n[m-2], new_n[m-1]
            k_result[i] = new_n
        return dfs(k_result, i+1, max_n, has_continuous_number)

    # max_n에 가깝게 만들어가는 과정
    swapped = False
    for j in range(m): 
        if swapped:
            break
        if max_n[j] != prev[j]:
            # max_n[j]가 prev에서 몇번째 인덱스에 위치하는지 찾는다.
            index_list = get_index_list(prev, max_n[j])

            for index in index_list:
                # prev의 j와 index를 swap한다.
                new_n = prev[:]
                new_n[j], new_n[index] = new_n[index], new_n[j]
                k_result[i] = new_n
                ret = max(ret, dfs(k_result, i+1, max_n, has_continuous_number))

            swapped = True
    return ret
    


# main
n, k = input().split()

# k = 연산 횟수
k = int(k)
# n = 입력받은 정수를 리스트로 변환
n = list(map(int, n))
# m = 자릿수
m = len(n)

# print(solve(n, m, k))
print(new_solve(n, m, k))

"""
n,k=381993,3

나온답: 998133

나와야할답: 998313
"""