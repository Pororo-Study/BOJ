grid = [list(map(int, input().split())) for _ in range(5)]

num_list = []
for _ in range(5):
    num_list += list(map(int, input().split()))

def check():
    cnt = 0

    # 가로
    for i in range(5):
        if grid[i] == [0] * 5:
            cnt += 1
    
    # 세로
    for i in range(5):
        if all(grid[j][i] == 0 for j in range(5)):
            cnt += 1
    
    # 우 위로 대각선
    if all(grid[i][i] == 0 for i in range(5)):
        cnt += 1
    
    # 우 아래로 대각선
    if all(grid[i][4 - i] == 0 for i in range(5)):
        cnt += 1
    
    return cnt

turn = 0
for idx in range(25):
    for x in range(5):
        for y in range(5):
            if num_list[idx] == grid[x][y]:
                grid[x][y] = 0
                turn += 1
                break
    if turn >= 12:
        ans = check()
        if ans >= 3:
            print(idx + 1)
            break
    