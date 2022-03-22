# 참고: https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-5639%EB%B2%88-%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC-Java-Python



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pre_to_post(start, end):
    if start > end:
        return
    
    root = preorder[start]

    # root보다 커지는 인덱스 찾기
    idx = start
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1
    
    # 왼쪽
    pre_to_post(start+1, idx-1)
    # 오른쪽
    pre_to_post(idx, end)
    # 루트
    print(root)


# 입력
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        # EOF -> break
        break

# pre_to_post
pre_to_post(0, len(preorder)-1)