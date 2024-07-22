import sys
input = sys.stdin.readline

while True:
    height = list(map(int, input().split()))
    if len(height) == 1 and height[0] == 0:
        break
    
    # stack에 height의 인덱스를 저장한다.
    stack = []
    max_area = 0 # 최대 넓이를 저장
    n = height[0]

    for i in range(len(height)):
        if i == 0:
            # 처음 주어지는 수는 직사각형의 수를 나타내므로 skip
            continue 

        if not stack:
            stack.append(i)
            continue

        # 스택의 꼭대기에 있는 막대보다 height[i]가 작을 경우
        if height[stack[-1]] > height[i]:
            # 스택에 들어 있는 막대로 만들 수 있는 넓이를 계산한다
            while stack:
                # 현재 막대보다 높이가 큰 것 까지만 꺼낸다
                top_idx = stack[-1]
                if height[top_idx] <= height[i]:
                    break
                
                pop_idx = stack.pop()
                if stack:
                    # 현재 인덱스 - 1 - 스택 꼭대기 인덱스
                    width = i - 1 - stack[-1]
                else:
                    # 현재 인덱스 - 1
                    width = i - 1
                area = width * height[pop_idx]
                if area > max_area:
                    max_area = area
        
        stack.append(i)
    
    # 스택에 남은 요소들을 처리한다
    while stack:
        pop_idx = stack.pop()
        if stack:
            width = n - stack[-1]
        else:
            width = n
        area = width * height[pop_idx]
        if area > max_area:
            max_area = area
    print(max_area)
