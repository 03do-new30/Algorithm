import sys
input = sys.stdin.readline

A, B = input().split()

min_ans = 50
for i in range(len(B) - len(A) + 1):
    tmp_ans = 0
    # print('----------')
    for j in range(len(A)):
        #print(A[j], "와, ", B[i+j], "를 비교")
        if A[j] != B[i+j]:
            tmp_ans += 1
    min_ans = min(min_ans, tmp_ans)
print(min_ans)
