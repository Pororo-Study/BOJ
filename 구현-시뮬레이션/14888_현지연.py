n = int(input())                                # 수의 개수
arr = list(map(int, input().split()))           # 수열
add, sub, mul, div = map(int, input().split())  # 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷) 개수
ans_max, ans_min = -int(1e9), int(1e9)          # 결과의 최댓값, 결과의 최솟값

def dfs(i, add, sub, mul, div, result):
    global ans_max, ans_min

    # 모든 연산을 다 한 경우, 최댓값과 최솟값 저장
    if i == n:
        ans_max = max(ans_max, result)
        ans_min = min(ans_min, result)
        return
    
    # 각 연산자의 개수가 남아있을경우, 재귀적으로 dfs 호출
    if add > 0:
        dfs(i + 1, add - 1, sub, mul, div, result + arr[i])
    if sub > 0:
        dfs(i + 1, add, sub - 1, mul, div, result - arr[i])
    if mul > 0:
        dfs(i + 1, add, sub, mul - 1, div, result * arr[i])
    if div > 0:
        dfs(i + 1, add, sub, mul, div - 1, int(result / arr[i]))    

dfs(1, add, sub, mul, div, arr[0])
print(ans_max)
print(ans_min)