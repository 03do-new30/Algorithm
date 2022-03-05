def solution(numbers, target):
    if not numbers and target == 0:
        return 1

    if not numbers:
        return 0

    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


"""
def solution(numbers, target):

    def solve(idx, curr):
        nonlocal answer

        if idx == len(numbers) and curr == target:
            answer += 1
            return

        if idx < len(numbers):
            solve(idx + 1, curr + numbers[idx])
            solve(idx + 1, curr - numbers[idx])

    answer = 0
    solve(0, 0)

    return answer


print(solution([4, 1, 2, 1]	, 4))
"""
