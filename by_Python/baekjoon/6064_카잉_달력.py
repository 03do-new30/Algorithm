import sys
input = sys.stdin.readline

# GCD (최대공약수)
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


t = int(input())
for _ in range(t):

    m, n, x, y = map(int, input().split())

    ### 1 ###
    # 달력의 마지막 해는 m, n 최소공배수!!!
    gcd = get_gcd(m, n)
    last_year = gcd * (m // gcd) * (n // gcd) # 최소공배수


    ### 2 ###
    # m * a + x 가 last_year보다 작을 때 검사하면서
    # 주어진 x:y가 만들어지는 해는 몇번째 해를 나타내는지 구하자
    a = 0
    year = -1
    while m * a + x <= last_year:
        tmp_year = m * a + x

        if (tmp_year - y) % n == 0:
            year = tmp_year
            break

        a += 1
    
    print(year)

