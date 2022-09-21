def k_jinsu(n, k):
    result = ""
    while n > 0:
        result = str(n%k) + result
        n = n // k
    return result

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    jinsu = k_jinsu(n, k)
    
    # 0을 기준으로 나눔
    parts = jinsu.split('0')
    
    answer = 0
    
    for part in parts:
        if len(part) == 0:
            continue
        
        if is_prime(int(part)):
            answer += 1
    
    return answer