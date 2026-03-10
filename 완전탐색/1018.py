# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

# 첫번째 풀이
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))

w_cnt_board = [[0] * m for _ in range(n)] # 맨 왼쪽 위 칸이 W인 보드 기준, 다시 칠해야 하는 칸
b_cnt_board = [[0] * m for _ in range(n)] # 맨 왼쪽 위 칸이 B인 보드 기준, 다시 칠해야 하는 칸
answer = 64

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0: # 짝짝
                if board[i][j] == 'B': # W여야하는데 B이면 w_cnt_board를 1로
                    w_cnt_board[i][j] = 1
                else:
                    b_cnt_board[i][j] = 1
            else: # 짝홀
                if board[i][j] == 'W':
                    w_cnt_board[i][j] = 1
                else:
                    b_cnt_board[i][j] = 1
        else:
            if j % 2 == 0: # 홀짝
                if board[i][j] == 'W':
                    w_cnt_board[i][j] = 1
                else:
                    b_cnt_board[i][j] = 1
            else: # 홀홀
                if board[i][j] == 'B':
                    w_cnt_board[i][j] = 1
                else:
                    b_cnt_board[i][j] = 1

for i in range(n-7):
    for j in range(m-7):
        w_cnt = 0 # 맨 왼쪽 위 칸이 W인 보드 기준, 다시 칠해야 하는 정사각형 개수
        b_cnt = 0 # 맨 왼쪽 위 칸이 B인 보드 기준, 다시 칠해야 하는 정사각형 개수
        for t in range(8):
            w_cnt += sum(w_cnt_board[i+t][j:j+8])
            b_cnt += sum(b_cnt_board[i+t][j:j+8])
        answer = min(answer, w_cnt, b_cnt)

print(answer)


# 두번째 풀이
# 공간복잡도 효율적
n, m = map(int, input().split())
board = [input() for _ in range(n)]
answer = 64

for i in range(n-7):
    for j in range(m-7):
        w_cnt = 0 # 맨 왼쪽 위 칸이 W인 보드 기준, 다시 칠해야 하는 정사각형 개수
        b_cnt = 0

        for x in range(8):
            for y in range(8):
                now = board[i+x][j+y] # 현재 칸

                if (x+y) % 2 == 0: # 짝짝, 홀홀
                    if now != 'W': # # W여야하는데 B이면 w_cnt에 1 더하기
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else: # 짝홀, 홀짝
                    if now != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1

        answer = min(answer, w_cnt, b_cnt)

print(answer)