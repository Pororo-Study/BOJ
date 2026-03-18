# 오목
# https://www.acmicpc.net/problem/2615

board = [list(map(int, input().split())) for _ in range(19)]

# 방향: ↗ → ↘ ↓
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]


for x in range(19):
    for y in range(19):
        if board[x][y] == 0:
            continue

        color = board[x][y] # 색깔 저장

        for d in range(4): # 4 방향
            cnt = 1

            # 5개 연속 확인
            for k in range(1, 5): 
                nx = x + dx[d]*k
                ny = y + dy[d]*k
                if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    cnt += 1
                else: # 한번이라도 다르면 멈춤
                    break
            
            # 5개면 추가 검사
            if cnt == 5:
                # 앞쪽 체크 (6목 방지)
                px = x - dx[d]
                py = y - dy[d]

                # 뒤쪽 체크 (6목 방지)
                nx = x + dx[d]*5
                ny = y + dy[d]*5

                if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == color:
                    continue
                if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    continue
                
                # 정답 출력
                print(color)
                print(x+1, y+1)
                exit()

print(0)