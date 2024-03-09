def solution(cap, n, deliveries, pickups):
    checks = [False] * n # 완료 여부
    dist = 0 # 총 이동한 거리
    
    while False in checks:
        truck = 0 # 창고에서 출발하는 트럭

        # 배달을 실시한 가장 먼 집의 거리
        far_delivery = -1

        # [배달] 끝집부터 검사
        for i in range(n-1, -1, -1):
            if deliveries[i] == 0:
                continue

            if truck >= cap:
                break

            if far_delivery < i:
                far_delivery = i

            if truck + deliveries[i] <= cap:
                truck += deliveries[i]
                deliveries[i] = 0
            else:
                possible = cap - truck
                deliveries[i] -= possible
                truck += possible
            print(i+1, "번째 집에서 택배 업무 진행")
            
            # 완료 여부 체크
            if deliveries[i] == 0 and pickups[i] == 0:
                checks[i] = True
        

        back_truck = 0 # 돌아오는 트럭

        # 수거를 실시한 가장 먼 집의 거리
        far_back = -1

        # [수거]
        for i in range(n-1, -1, -1):
            if pickups[i] == 0:
                continue

            if back_truck >= cap:
                break

            if far_back < i:
                far_back = i

            if back_truck + pickups[i] <= cap:
                back_truck += pickups[i]
                pickups[i] = 0
            else:
                possible = cap - back_truck
                pickups[i] -= possible
                back_truck += possible
            print(i+1, "번째 집에서 수거 업무 진행")
            
            # 완료 여부 체크
            if deliveries[i] == 0 and pickups[i] == 0:
                checks[i] = True
        
        print("배달한 가장 먼 집의 거리는", far_delivery + 1)
        print("수거한 가장 먼 집의 거리는", far_back + 1)


        dist += max(far_delivery + 1, far_back + 1) * 2

        print('~' * 20)
    print("dist:", dist)
    return dist


cap = [4, 2]
n = [5, 7]
deliveries = [
    [1, 0, 3, 1, 2]	,
    [1, 0, 2, 0, 1, 0, 2]	
]
pickups = [
    [0, 3, 0, 4, 0],
    [0, 2, 0, 1, 0, 2, 0]	
]
result = [16, 30]

for i in range(2):
    print(result[i] == solution(cap[i], n[i], deliveries[i], pickups[i]))
    print('-' * 40)