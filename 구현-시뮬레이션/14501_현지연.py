# 풀이 1
# DFS
n = int(input())    # 전체 상담 개수
t_list = []         # 각 상담을 완료하는 데 걸리는 기간
p_list = []         # 각 상담을 완료했을 때 받을 수 있는 금액
answer = 0

# 데이터 저장
for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

def dfs(idx, profit):
    global answer
    # N+1일째에는 회사에 없기 때문에, 상담을 할 수 없으므로 종료
    if idx > n:
        return
    # 상담 마지막 날, 이익의 최댓값 저장하고 종료
    if idx == n:
        answer = max(answer, profit)
        return
    # 상담을 안하는 경우
    dfs(idx + 1, profit)
    # 상담을 하는 경우
    dfs(idx + t_list[idx], profit + p_list[idx])

dfs(0, 0)
print(answer)


# 풀이 2
# DP
n = int(input())    # 전체 상담 개수
t = []              # 각 상담을 완료하는 데 걸리는 기간
p = []              # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
                    # i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i # 상담이 끝나는 날짜
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)