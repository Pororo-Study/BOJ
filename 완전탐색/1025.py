# 제곱수 찾기
# https://www.acmicpc.net/problem/1025


# 완전탐색
n, m = map(int, input().split())
board = [input() for _ in range(n)]
answer = -1

for i in range(n):
    for j in range(m):
        for dx in range(-n+1, n):
            for dy in range(-m+1, m):

                x, y = i, j
                num = "" # 문자열로 이어붙이기

                # dx,dy가 (0,0)일때는 자기 자신 한 번만 반복하도록
                if dx == 0 and dy == 0:
                    num += board[x][y]
                    val = int(num)
                    root = int(val ** 0.5)
                    if root * root == val:
                        answer = max(answer, val)
                    continue

                while 0 <= x < n and 0 <= y < m:
                    num += board[x][y] # 숫자 이어붙이기

                    val = int(num)
                    root = int(val ** 0.5) # 제곱근 내림

                    if root * root == val: 
                    # if int(num) ** 0.5.is_integer():
                        answer = max(answer, val)

                    x += dx
                    y += dy

print(answer)


# 첫번째 풀이
# 정답은 통과됐지만 테스트케이스에 없는 오류가 있음
n, m = map(int, input().split())
board = [input() for _ in range(n)]
answer = -1

for i in range(n):
    for j in range(m):
        for a in range(-n+1, n):
            for b in range(-m+1, m):
                num = ""

                for k in range(9): # 쭉 이동하기 위해 반복
                    
                    x = i + a * k
                    y = j + b * k
                    
                    if x < 0 or x >= n or y < 0 or y >= m:
                        break

                    num += board[x][y] # 숫자 이어붙이기

                    calc = int(num) ** 0.5 # 제곱근

                    if calc.is_integer(): # 완전제곱은은 제곱근이 정수
                        answer = max(answer, int(num))
print(answer)