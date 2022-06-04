import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
H, W = map(int, input().split())
cheese = []
for _ in range(H):
    cheese.append(list(map(int, input().split())))

index_x = [0, 1, 0, -1]
index_y = [1, 0, -1, 0]

def check_index(x, y):
    if(x>=0 and x<= H-1 and y>=0 and y<=W-1):
        return True
    else:
        return False

def find_air(x, y):
    if(cheese[x][y] == 0):
        cheese[x][y] = -1
        for i in range(4):
            if(check_index(x+index_x[i], y+index_y[i])):
                find_air(x+index_x[i], y+index_y[i])

find_air(0,0)
print(cheese)

def in_air(x, y):
    for i in range(4):
        if(check_index(x+index_x[i], y+index_y[i])):
            if(cheese[x+index_x[i]][y+index_y[i]] == time*(-1)):
                return True
    
    return False
                    
def become_air(x, y):
    for i in range(4):
        if(cheese[x+index_x[i]][y+index_y[i]] < 0):
            cheese[x][y] = (time+1)*(-1)
            for j in range(4):
                if(cheese[x+index_x[j]][y+index_y[j]] == 0):
                    become_air(x+index_x[j], y+index_y[j])
            return
    
time = 0
pre_cheese_count = 0
cheese_count = 0
while(1):
    sw = 0
    time += 1
    print("=============", time, "=============")
    for i in range(H):
        for j in range(W):
            print(cheese[i][j], end = " ")
            if(cheese[i][j] == 1):
                cheese_count += 1
                if(in_air(i, j)):
                    cheese[i][j] = (time+1) * (-1)
                sw = 1


        print("")
    for i in range(H):
        for j in range(W):
            if(cheese[i][j] == 0):
                become_air(i, j)
    if(sw==0):
        break
    pre_cheese_count = cheese_count
    cheese_count = 0
print(time-1, pre_cheese_count)