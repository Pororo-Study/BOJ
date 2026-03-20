# 꽃길
# https://www.acmicpc.net/problem/14620
# DFS

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 0, 1, -1] # 모든 꽃잎 위치 5좌표
dy = [0, 1, -1, 0, 0]

visited = [[False]*n for _ in range(n)] # 방문 여부 저장
answer = float('inf') # 꽃을 심기 위한 최소 비용


def dfs(cnt, total):
    global answer

    # 꽃 3개 다 심었으면 최소 비용 저장
    if cnt == 3:
        answer = min(answer, total)
        return
    
    for x in range(1, n-1): # 꽃잎이 밖으로 나가지 않는 중심 위치
        for y in range(1, n-1):
            cost = 0 # 꽃의 비용
            check = True # 꽃 심기 성공 여부
            xy_temp = [] # 꽃의 5개 좌표 저장

            # 꽃 5칸 체크
            for k in range(5):
                nx = x + dx[k]
                ny = y + dy[k]
                if visited[nx][ny]: # 하나라도 다른 꽃과 겹치면 멈추기
                    check = False
                    break

                xy_temp.append((nx, ny))
                cost += board[nx][ny] 

            # 설치할 수 없는 꽃이므로 다음 반복문으로 넘어가기
            if not check:
                continue
            
            # 방문처리
            for i, j in xy_temp:
                visited[i][j] = True

            dfs(cnt+1, total+cost) # 꽃 개수 +1, 꽃 하나 비용 더하기

            # 되돌리기(백트래킹)
            for i, j in xy_temp:
                visited[i][j] = False

dfs(0, 0)
print(answer)