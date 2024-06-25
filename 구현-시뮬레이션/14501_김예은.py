N = int(input())
schedule = [list(map(int, input().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N): # i번째날까지 일했을 때 얻을 수 있는 최대 수익을 구해보자
	for j in range(i+schedule[i][0], N+1): # i번째날에 상담을 진행했을 때 상담이 가능한 모든 날짜의 최대 수익을 구한다. ( "i+상담기간" 부터 "마지막날" 까지)
		if dp[j] < dp[i]+schedule[i][1]: # j번째 날에 상담을 진행했을때 얻을 수 있는 최대 수익 입력
			dp[j] = dp[i]+schedule[i][1]
print(dp[-1])