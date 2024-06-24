from collections import deque

# 톱니바퀴의 상태 입력받고 저장하기
wheel = []
for i in range(4):
    wheel.append(deque(list(input())))

# 회전 횟수 입력 받기
k = int(input())

for _ in range(k):
    i, direction = map(int, input().split())    # 회전시킨 톱니바퀴의 번호, 방향
    i = i - 1                                   # 톱니바퀴 번호를 0 ~ 3으로 변경
    now_left = wheel[i][6]                      # 현재 톱니바퀴의 왼쪽 극
    now_right = wheel[i][2]                     # 현재 톱니바퀴의 오른쪽 극
    check = [0, 0, 0, 0]                        # 회전 가능 여부
    check[i] = 1                                # 현재 톱니바퀴 회전 가능 체크

    # 왼쪽 톱니바퀴 확인하기
    if 0 < i:
        for l in range(i - 1, -1, -1):
            if wheel[l][2] != now_left:
                check[l] = 1
                now_left = wheel[l][6]
            else:       # 회전 불가능하다면 멈춤
                break
    # 오른쪽 톱니바퀴 확인하기
    if i < 3:
        for r in range(i + 1, 4):
            if wheel[r][6] != now_right:
                check[r] = 1
                now_right = wheel[r][2]
            else:       # 회전 불가능하다면 멈춤
                break
    
    if direction == 1:
        # 현재 톱니바퀴와 다다음 톱니바퀴는 시계 방향으로 회전
        for c in [i, (i + 2) % 4]:
            if check[c]:
                wheel[c].appendleft(wheel[c].pop())
        # 나머지 톱니바퀴는 반시계 방향으로 회전
        for c in [(i + 1) % 4, (i + 3) % 4]:
            if check[c]:
                wheel[c].append(wheel[c].popleft())
    else:
        # 현재 톱니바퀴와 다다음 톱니바퀴는 반시계 방향으로 회전
        for c in [i, (i + 2) % 4]:
            if check[c]:
                wheel[c].append(wheel[c].popleft())
        # 나머지 톱니바퀴는 시계 방향으로 회전
        for c in [(i + 1) % 4, (i + 3) % 4]:
            if check[c]:
                wheel[c].appendleft(wheel[c].pop())

# 점수 계산
answer = 0
for i in range(4):
    answer += (int(wheel[i][0]) * 2**i)

print(answer)