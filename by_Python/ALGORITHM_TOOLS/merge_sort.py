arr = [5, 3, 2, 9, 7, 4, 1]

def merge_sort(start, end):
    if start == end:
        return
    
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    print("[merge] start:", start, "end:", end)
    merge(start, end)

def merge(start, end):
    tmp = [-1] * (end - start + 1)
    mid = (start + end) // 2
    i = start; j = mid + 1
    k = 0 # tmp의 index
    
    print("left:", arr[start:mid+1])
    print("right:", arr[j:end+1])
    while i <= mid and j <= end:
        # print("i:", i, "j:", j)
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
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
    print("tmp:", tmp)
    print("arr:", arr)
    print("-" * 30)
merge_sort(0, len(arr)-1)
print("arr:", arr)