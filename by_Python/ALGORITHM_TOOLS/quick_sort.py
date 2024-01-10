arr = [5, 1, 4, 2, 8, 2, 5, 4, 6, 1, 9, 6, 9, 1]

def choose_pivot(start, end):
    # pivot은 그냥 중간에 있는 값으로 정한다고 하자
    return (start + end) // 2

def quick_sort(start, end):
    if start < end:
        pivot_idx = partition(start, end)
        quick_sort(start, pivot_idx - 1)
        quick_sort(pivot_idx + 1, end)

def partition(start, end):
    pivot_idx = choose_pivot(start, end)
    pivot_val = arr[pivot_idx]
    # pivot을 맨 뒤로 보낸다
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]

    store_idx = start

    for i in range(start, end + 1):
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    
    arr[store_idx], arr[end] = arr[end], arr[store_idx]
    print("pivot value:", pivot_val, "pivot_idx", pivot_idx, "start:", start, " end:", end)
    print("-> arr:", arr)
    print()
    return store_idx


print("arr:", arr)
quick_sort(0, len(arr)-1)
print("arr:", arr)