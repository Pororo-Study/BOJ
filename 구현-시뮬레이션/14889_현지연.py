from itertools import combinations

n = int(input())    # 사람 수
s = [list(map(int, input().split())) for _ in range(n)] # 능력치
answer = int(1e9)

# 조합을 사용해 모든 경우의 수 계산
for start_team in list(combinations(range(n), n // 2)):     # 스타트 팀 뽑기
    link_team = [x for x in range(n) if x not in start_team]    # 스타트 팀이 아닌 사람은 링크 팀

    result = 0  # 두 팀의 능력치 차이
    for i in range((n // 2) - 1):
        for j in range(i + 1, n // 2):
            result += s[start_team[i]][start_team[j]] + s[start_team[j]][start_team[i]]     # 스타트 팀의 능력치는 더하기
            result -= s[link_team[i]][link_team[j]] + s[link_team[j]][link_team[i]]         # 링크 팀의 능력치는 빼기

    answer = min(answer, abs(result))   # 절댓값을 적용하고 최솟값 저장

print(answer)