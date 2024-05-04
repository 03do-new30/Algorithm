# 출처: https://velog.io/@carrotcookie/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-PCCP-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-3%EB%B2%88
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2

    # next 기준으로 계산하므로 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1
    
    while startTime < endTime:
        # 시침: 1시간 30도 -> 1초에 1/120도
        # 분침: 1분에 6도 -> 1초에 1/10도
        # 초침: 1초에 6도
        hCurAngle = startTime / 120 % 360
        mCurAngle = startTime / 10 % 360
        sCurAngle = startTime * 6 % 360

        # 다음 위치가 360도가 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        # 이동했을 때 지나쳤거나 같아졌는지를 비교하는 것이므로 현재 위치는 해줄 필요 없다
        hNextAngle = (startTime + 1) / 120 % 360
        if hNextAngle == 0:
            hNextAngle = 360
        mNextAngle = (startTime + 1) / 10 % 360
        if mNextAngle == 0:
            mNextAngle = 360
        sNextAngle = (startTime + 1) * 6 % 360
        if sNextAngle == 0:
            sNextAngle = 360
        
        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        # 시침과 분침이 동시에 겹쳤을 때 중복 카운팅 제외
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1
        startTime += 1
    
    return answer

h1 = [0, 12, 0, 11, 11, 1, 0]
m1 = [5, 0, 6, 59, 58, 5, 0]
s1 = [30, 0, 1, 30, 59, 5, 0]
h2 = [0, 12, 0, 12, 11, 1, 23]
m2 = [7, 0, 6, 0, 59, 5, 59]
s2 = [0, 30, 6, 0, 0, 6, 59]
result = [2, 1, 0, 1, 1, 2, 2852]

for i in range(len(result)):
    print(solution(h1[i], m1[i], s1[i], h2[i], m2[i], s2[i]) == result[i])