from cmath import inf
import sys
input = sys.stdin.readline
N = int(input())
population = []
pos = []
dist = 0
total_population = [0]
for i in range(N):
    population.append(list(map(int, input().split())))

population.sort(key = lambda x:x[0])
for i in range(N):
    dist += (population[i][0]-population[0][0]) * population[i][1]
    total_population.append(total_population[-1] + population[i][1])
    pos.append(population[i][0])

total_population.pop(0)

# print(population)
# print(total_population)
# print(pos)

min_dist = dist
ans = population[0][0]
for i in range(1, N):
    # print(pos[i-1], "=>", pos[i], ":", dist, "=>", end = " ")
    dist_dif = pos[i] - pos[i-1]
    dist += dist_dif * total_population[i-1]
    dist -= dist_dif * (total_population[-1] - total_population[i-1])
    if(dist < min_dist):
        ans = pos[i]
        min_dist = dist
    # print(dist)
print(ans)