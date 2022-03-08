from collections import deque


def solution(begin, target, words):
    visited = [False]*len(words)

    q = deque([(begin, 0)])
    while q:
        current, change_cnt = q.popleft()
        if current == target:
            return change_cnt

        for i in range(len(words)):
            if diff(current, words[i]) == 1 and not visited[i]:
                q.append((words[i], change_cnt + 1))
                visited[i] = True
    return 0


def diff(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
