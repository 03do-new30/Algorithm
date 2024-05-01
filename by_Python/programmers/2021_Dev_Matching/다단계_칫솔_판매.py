def solution(enroll, referral, seller, amount):
    
    answer = [0] * len(enroll)
    
    member_idx = dict()
    for i in range(len(enroll)):
        member_idx[enroll[i]] = i

    def add_value(idx, price):
        share = int((price * 0.1) // 1)
        if share < 1:
            answer[idx] += price
            return
        answer[idx] += price - share
        parent = referral[idx]
        if parent == '-':
            return
        add_value(member_idx[parent], share)
    
    for i in range(len(seller)):
        seller_name = seller[i]
        price = amount[i] * 100
        add_value(member_idx[seller_name], price)

    return answer

enroll = [
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
]
referral = [
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
]
seller = [
    ["young", "john", "tod", "emily", "mary"],
    ["sam", "emily", "jaimie", "edward"]
]
amount = [
    [12, 4, 2, 5, 10],
    [2, 3, 5, 4]
]
result = [
    [360, 958, 108, 0, 450, 18, 180, 1080],
    [0, 110, 378, 180, 270, 450, 0, 0] 
]

for i in range(len(result)):
    print(solution(enroll[i], referral[i], seller[i], amount[i]) == result[i])