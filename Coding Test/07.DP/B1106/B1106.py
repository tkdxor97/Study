import sys
import math
input = sys.stdin.readline
C, N = map(int, input().split())
cost = []


for _ in range(N):
    cost.append(list(map(int, input().split())))
    
cost.sort(key = lambda x:(-x[1]/x[0], x[0]))
