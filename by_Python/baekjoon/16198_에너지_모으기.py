import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

def solve(beads, energy):
    if len(beads) == 2:
        return energy
    
    ans = -1
    for i in range(1, len(beads) - 1):
        new_beads = []
        for j in range(len(beads)):
            if i != j:
                new_beads.append(beads[j])
        ret = solve(new_beads, energy + beads[i-1] * beads[i+1])
        
        if ans == -1 or ans < ret:
            ans = ret
    return ans

answer = solve(w, 0)
print(answer)