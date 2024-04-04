# 양의 정수 n을 k진수로 바꾼다
def convert_k(n, k):
    ret = ""
    while n > 0:
        ret = str(n % k) + ret
        n = n // k
    return ret

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True

def solution(n, k):
    k_base = convert_k(n, k)
    
    split_0 = k_base.split('0')
    numbers = []
    for s in split_0:
        if len(s) == 0:
            continue
        numbers.append(int(s))
    if len(numbers) == 0:
        return 0

    answer = 0
    for num in numbers:
        # 소수인지 판별한다
        if is_prime(num):
            answer += 1

    return answer

n = [437674, 110011, 1]
k = [3, 10, 3]
result = [3, 2]
for i in range(len(result)):
    print(solution(n[i], k[i]) == result[i])
    print('-' * 40)