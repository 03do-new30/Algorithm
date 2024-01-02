import sys
input = sys.stdin.readline

n = list(map(int, (list(input().strip()))))

"""
2 * 3 * 5 = 30
2의 배수 : 마지막 자리가 짝수
3의 배수 : 각 자리의 합이 3으로 나누어 떨어짐
5의 배수 : 마지막 자리가 0 또는 5
=> 30의 배수 : 마지막 자리가 0이고 각 자리의 합이 3으로 나누어 떨어짐

각 자리의 합은 숫자의 순서가 바뀌어도 불변
내림차순으로 정렬한 뒤, 마지막 숫자가 0이 오게끔 만들 수 있으면 됨
"""

n.sort(reverse=True)

# 각 자리의 합이 3으로 나누어 떨어지는가?
if sum(n) % 3 == 0:
    # 내림차순으로 정렬했을 때 마지막 숫자에 0이 오는지 확인
    if n[-1] == 0:
        ans = 0
        ten = 1
        for i in range(len(n)-1, -1, -1):
            ans += n[i] * ten
            ten *= 10
        print(ans)
    else:
        print(-1)
else:
    print(-1)

