import copy
from collections import defaultdict

routes = []


def solution(tickets):
    # dictionary
    info = defaultdict(list)
    for ticket in tickets:
        a, b = ticket
        info[a].append(b)

    dfs(tickets, info, "ICN", 0, "ICN")
    routes.sort()
    answer = routes[0].split()
    return answer


def dfs(tickets, info, start, cnt, route):
    if cnt == len(tickets):
        routes.append(route)
        return

    if start in info:
        for end in info[start]:
            new_info = copy.deepcopy(info)
            new_info[start].remove(end)
            dfs(tickets, new_info, end, cnt + 1, route + " " + end)


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
ret = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution(tickets) == ret)
