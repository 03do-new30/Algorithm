def solution(phone_book):
    phone_book = sorted(phone_book)  # 사전순 정렬

    for i in range(len(phone_book)-1):
        num1 = phone_book[i]
        num2 = phone_book[i+1]
        if num2.startswith(num1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
