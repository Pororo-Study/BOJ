# 퇴사
# https://www.acmicpc.net/problem/14501
# DP

n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):

    # 상담이 퇴사 전에 끝나는 경우
    if i + t[i] <= n:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i]) # 상담을 안하거나, 하거나

    # 상담 못하는 경우
    else:
        dp[i] = dp[i+1] 

print(dp[0])