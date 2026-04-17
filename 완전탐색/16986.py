# 인싸들의 가위바위보
# https://www.acmicpc.net/problem/16986

# 완전탐색
# 구현/시뮬레이션

from itertools import permutations # 순열

n, k = map(int, input().split()) # 손동작 수 n, 우승을 위해 필요한 승수 k
board = [list(map(int, input().split())) for _ in range(n)] # 상성 정보 a_ij
# 0: j가 이김
# 1: 비김
# 2: i가 이김

손동작 = [[], [], []] # 세 사람의 손동작 순서
# 0 지우
손동작[1] = list(map(int, input().split())) # 1 경희
손동작[2] = list(map(int, input().split())) # 2 민호
answer = 0

for jiwoo in list(permutations(range(1,n+1), n)): # 지우의 손동작

    win = [0, 0, 0] # 세 사람의 승수
    fight = (0, 1) # 현재 대결 상대
    next_fight = 2 # 다음 대결 상대
    idx = [0, 0, 0] # 세 사람의 손동작 idx

    손동작[0] = list(jiwoo) # 지우 손동작 초기화
    
    # 지우가 이기거나 지우가 n번 싸울때까지 반복
    while answer == 0 and idx[0] < n:
        x, y = fight # 대결 상대

        # 손동작[x] : x의 손동작
        # idx[x]: x의 손동작 인덱스
        # 손동작은 1~n 이므로 -1 해줘야 함 

        # x가 이김
        if board[손동작[x][idx[x]] - 1][손동작[y][idx[y]] - 1] == 2: 
            fight = (x, next_fight) # 다음 대결 상대
            next_fight = y # 진 사람은 다다음 대결 상대가 됨
            win[x] += 1 # x의 승수 +1

        # y가 이김
        elif board[손동작[x][idx[x]] - 1][손동작[y][idx[y]] - 1] == 0:
            fight = (y, next_fight)
            next_fight = x
            win[y] += 1
        
        # 비김 -> max가 이김
        else:
            fight = (max(x, y), next_fight) # x, y중 큰 값이 이김
            next_fight = min(x, y)
            win[max(x, y)] += 1

        idx[x] += 1 # 현재 대결을 했으므로 손동작 인덱스 +1
        idx[y] += 1

        # 지우가 우승
        if win[0] == k:
            answer = 1
            break
        # 경희 또는 민호가 우승
        elif win[1] == k or win[2] == k:
            break

print(answer)