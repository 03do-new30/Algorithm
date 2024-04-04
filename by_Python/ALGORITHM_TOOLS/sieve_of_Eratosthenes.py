# 에라토스테네스의 체
max_num = 1000000
primes= [True] * (max_num + 1)
primes[1] = False
for i in range(2, max_num + 1):
    if primes[i]:
        for j in range(i+i, max_num + 1, i):
            primes[j] = False

print("2는 소수인가?:", primes[2])
print("369는 소수인가?", primes[369])
print("17은 소수인가?", primes[17])