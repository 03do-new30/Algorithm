def solution(board, moves):
    answer = 0
    
    # 바구니
    basket = []
    
    for move in moves:
        idx = move - 1
        for row in board:
            if row[idx] > 0: # 인형을 만난 경우
                # basket이 비어있으면 추가하고 종료
                if not basket:
                    basket.append(row[idx])
                    row[idx] = 0
                    break

                # basket에 인형이 연속인지 확인
                if row[idx] == basket[-1]:
                    basket.pop() # pop
                    answer += 2 # 인형 개수 추가
                else:
                    basket.append(row[idx])
                row[idx] = 0
                break
        
    
    return answer