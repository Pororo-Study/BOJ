from collections import defaultdict

bingo = [0] * (26)  

# 숫자 인덱스 위치에 빙고판 (i, j) 저장
for i in range(5):
    chulsoo = list(map(int, input().split()))   # 철수의 입력
    for j in range(5):
        bingo[chulsoo[j]] = (i, j)

row_dic = defaultdict(list)     # 행 딕셔너리
col_dict = defaultdict(list)    # 열 딕셔너리
x_dict = defaultdict(list)      # 대각선 딕셔너리
answer = 25

for k in range(5):
    mc = list(map(int, input().split()))    # 사회자의 입력
    for t in range(5):
        i, j = bingo[mc[t]]                 # 사회자가 부르는 수의 빙고판 i, j 위치
        row_dic[i].append(j)                # 행 딕셔너리에 열 번호 추가
        col_dict[j].append(i)               # 열 딕셔너리에 행 번호 추가
        if i == j:                          # 오른쪽 대각선 추가
            x_dict['right'].append(i)
        if i + j == 4:                      # 왼쪽 대각선 추가
            x_dict['left'].append(i)

        cnt = 0                             # 빙고 선의 개수
        for arr in row_dic.values():        # 딕셔너리에 value의 길이가 5이면 개수 카운트
            if len(arr) == 5:
                cnt += 1
        for arr in col_dict.values():
            if len(arr) == 5:
                cnt += 1
        for arr in x_dict.values():
            if len(arr) == 5:
                cnt += 1
            
        if cnt >= 3:                        # 선이 3개이면 빙고 외치기
            answer = min(answer, ((k * 5) + (t+1))) # 가장 먼저 외치기

print(answer)   