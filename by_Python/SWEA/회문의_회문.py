import sys
sys.stdin = open("by_Python/SWEA/inputs/회문의_회문.txt", "r")

# string이 회문인지 검사한다
# 회문: 앞에서부터 뒤로 읽은 것과 뒤에서부터 앞으로 읽은 것이 동일하다
def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
        

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    # S는 회문인가?
    if is_palindrome(string):
        mid = len(string) // 2
        left = string[:mid]
        right = string[mid+1:]
        if is_palindrome(left) and is_palindrome(right):
            print("#{0} YES".format(test_case))
        else:
            print("#{0} NO".format(test_case))
    else:
        print("#{0} NO".format(test_case))