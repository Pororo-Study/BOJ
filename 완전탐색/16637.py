# 괄호 추가하기
# https://www.acmicpc.net/problem/16637

# 완전탐색
# DFS
n = int(input())
formula = input() # 입력받은 수식
visited = [False] * n # 연산자 괄호 여부
answer = -(2**31)

t = ((n // 2) + 1) // 2 # 괄호의 최대 갯수

# 숫자 하나만 입력 받았을 경우 바로 출력 후 종료
if t == 0:
    print(formula)
    exit()

# 수식 계산하기
def calculate():
    # 괄호 먼저 1차 계산
    f = [int(formula[0])] # 숫자와 연산자를 원소로 넣을 수식 리스트
    for i in range(1, n, 2): # 연산자만 확인
        # 괄호가 있으면 계산해서 넣기
        if visited[i]:
            f.append(eval(str(f.pop())+formula[i:i+2]))
        # 괄호가 없으면 연산자와 숫자 그대로 넣기
        else: 
            f.append(formula[i])
            f.append(int(formula[i+1]))
    # print(f)

    # 순서대로 2차 계산
    result = int(f[0])
    for i in range(1, len(f), 2):
        op = f[i]
        if op == "+":
            result += f[i+1]
        elif op == "-":
            result -= f[i+1]
        elif op == "*":
            result *= f[i+1]

    return result


def dfs(idx, cnt): # 현재 인덱스, 괄호의 개수
    global answer

    if cnt == t or idx == n-2: # 연산자 최대 개수에 도달하거나 모든 연산자를 검토했다면
        # print(idx, cnt, visited)
        answer = max(answer, calculate())
        return
    
    dfs(idx+2, cnt) # 괄호 추가 안하고 다음 연산자 인덱스 확인
    
    if not visited[idx]: # 현재 연산자에 괄호가 없다면
        visited[idx+2] = True # 다음 연산자 괄호 표시
        dfs(idx+2, cnt+1) # 괄호 추가하고 다음 연산자 인덱스 확인
        visited[idx+2] = False # 되돌리기


dfs(1, 0) # 첫번째 연산자 괄호 없음
visited[1] = True 
dfs(1, 1) # 첫번째 연산자 괄호 있음
visited[1] = False

print(answer)