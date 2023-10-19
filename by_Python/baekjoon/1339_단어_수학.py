import sys
input = sys.stdin.readline

# 참고 출처: https://yoonsang-it.tistory.com/41

n = int(input())

alphabet_dict = dict()
for i in range(65, 91):
    alphabet_dict[chr(i)] = 0

words = []
for _ in range(n):
    words.append(input().strip())

for word in words:
    for i in range(len(word)):
        num = 10 ** (len(word) - i - 1)
        let = word[i]
        alphabet_dict[let] += num

alphabet_list = []
for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
answer = 0
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)