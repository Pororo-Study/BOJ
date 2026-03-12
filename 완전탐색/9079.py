# 동전 게임
# https://www.acmicpc.net/problem/9079

from collections import deque

ops = [ # 8가지 뒤집기 연산을 비트마스크로 정의
    0b111000000,  # row0: 첫 번째 행 뒤집기
    0b000111000,  # row1: 두 번째 행 뒤집기
    0b000000111,  # row2: 세 번째 행 뒤집기
    0b100100100,  # col0: 첫 번째 열 뒤집기
    0b010010010,  # col1: 두 번째 열 뒤집기
    0b001001001,  # col2: 세 번째 열 뒤집기
    0b100010001,  # diag ↘ 대각선
    0b001010100   # diag ↙ 대각선
]


t = int(input()) # 테스트케이스 개수

for _ in range(t):

    initial = 0 # 현재 보드 상태를 9비트 정수로 표현
    flag = False # # 모든 면이 같아지는 경우 찾았는지 여부

    # 3×3 보드 입력
    for i in range(3):
        row = input().split()
        for j in range(3):
            if row[j] == "H":
                # H 이면 해당 위치 비트를 1로 설정
                initial |= 1 << (i*3 + j) # i*3 + j: 2차원 좌표를 1차원 비트 위치로 변환

    # BFS
    q = deque([(initial, 0)]) # (state, 뒤집기 횟수)
    visited = set([initial]) # 방문 여부

    while q:
        state, cnt = q.popleft() # # 현재 상태와 연산 횟수 꺼내기

        # 목표 상태 확인: 모두 T(0) 또는 모두 H(1) = 511(0b111111111)
        if state == 0 or state == 511:
            print(cnt)
            flag = True # 최소 연산 횟수 출력
            break
        
        # 8가지 연산 적용
        for op in ops:
            nxt = state ^ op # XOR: 해당 연산 위치 비트 뒤집기

            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cnt+1))

    # BFS 끝까지 목표 상태 못 찾으면 -1 출력
    if not flag:
        print(-1)