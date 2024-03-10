def solution(cap, n, deliveries, pickups):
    print("cap:", cap)
    dist = 0
    deli_stack = []
    pick_stack = []
    for i in range(n):
        if deliveries[i] > 0:
            deli_stack.append((i+1, deliveries[i])) #(집 번호, 배달할 택배)
        if pickups[i] > 0:
            pick_stack.append((i+1, pickups[i]))
    
    while len(deli_stack) > 0 or len(pick_stack) > 0:
        truck = 0
        # 배달 단계
        # 현재 가야하는 가장 먼 집
        far_deli = deli_stack[-1][0] if deli_stack else -1
        far_pick = pick_stack[-1][0] if pick_stack else -1
        far_house = max(far_deli, far_pick)
        print(far_house, '번 집으로 슝슝')
        while deli_stack and truck < cap:
            house, box = deli_stack.pop()
            # 배송 가능한 택배 개수
            possible = cap - truck
            if box <= possible:
                truck += box
                print(house,'번 집에', box, '개 배송')
            else:
                truck += possible
                deli_stack.append((house, box - possible)) # 남은 택배는 스택에 다시 넣어둔다
                print(house,'번 집에', possible, '개 배송')
        # 수거 단계
        back_truck = 0
        while pick_stack and back_truck < cap:
            house, box = pick_stack.pop()
            # 수거 가능한 택배 개수
            possible = cap - back_truck
            if box <= possible:
                back_truck += box
                print(house,'번 집에서', box, '개 수거')
            else:
                back_truck += possible
                pick_stack.append((house, box - possible))
                print(house,'번 집에서', possible, '개 수거')
        print('~' * 20)
        dist += far_house * 2
    print("dist:", dist)
    return dist


cap = [4, 2, 1, 2, 3]
n = [5, 7, 5, 2, 2]
deliveries = [
    [1, 0, 3, 1, 2]	,
    [1, 0, 2, 0, 1, 0, 2],
    [0, 0, 1, 0, 0],
    [0, 0],
    [2, 4]
]
pickups = [
    [0, 3, 0, 4, 0],
    [0, 2, 0, 1, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 4],
    [4, 2]
]
result = [16, 30, 6, 8, 8]

for i in range(len(result)):
    print(result[i] == solution(cap[i], n[i], deliveries[i], pickups[i]))
    print('-' * 40)