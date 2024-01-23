import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0

# merge sort로 풀어서 시간 복잡도 줄일 수 있음
def merge_sort(start, end):
    if start == end:
        return
    
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    merge(start, end)

def merge(start, end):
    global cnt

    tmp = [-1] * (end - start + 1)
    mid = (start + end) // 2
    i = start; j = mid + 1
    k = 0 # tmp의 index

    # print("left:", arr[start:mid+1])
    # print("right:", arr[j:end+1])   

    while i <= mid and j <= end:
        # print("i:", i, "j:", j)
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            # 오른쪽 절반이 이동할 떄, 왼쪽 절반에서 아직 이동하지 않은 것의 개수가 그떄의 inversion의 개수이다!
            cnt += (mid-i+1)
            tmp[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1
    
    while j <= end:
        tmp[k] = arr[j]
        k += 1
        j += 1
    
    for idx in range(start, end + 1):
        arr[idx] = tmp[idx - start]
    
    # print("tmp:", tmp, ", arr:", arr)
    # print("-" * 30)

merge_sort(0, len(arr)-1)
print(cnt)