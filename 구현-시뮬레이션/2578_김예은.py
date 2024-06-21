# 빙고판
bingo = [0]*5

# 채우기
for i in range(5):
    n = list(map(int, input().split()))
    bingo[i] = n

# 사회자가 부르는 수
num = []
for i in range(5):
    n = list(map(int, input().split()))
    num += n



for i in range(25):
    count = 0 # 횟수
    # print(num[i])

    # 0으로 변경
    for j in range(5):
        # print(bingo[j])
        if num[i] in bingo[j]:
            ind = bingo[j].index(num[i])
            bingo[j][ind] = 0
    
    # for r in range(5):
    #     for c in range(5):
    #         print(bingo[r][c], end=' ')
    #     print()
    # print('-'*5)


    # 가로, 세로, 대각선 확인
    for j in range(5):
        if sum(bingo[j][k] for k in range(5)) == 0:
            count += 1
        if sum(bingo[k][j] for k in range(5)) == 0:
            count += 1
    
    if bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4] == 0:
        count += 1  
    if bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0] == 0:
        count += 1

    if count >=3:
        print(i+1)
        break    