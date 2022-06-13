from itertools import permutations
import sys
input = sys.stdin.readline



N, M = map(int, input().split())
nums = map(int, input().split())
combis = sorted(list(set((permutations(nums, M)))))

for combi in combis:
    print(' '.join(map(str, combi)))