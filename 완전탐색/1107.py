# 리모컨
# https://www.acmicpc.net/problem/1107


# 첫번째 풀이
n = int(input()) # 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수

if m == 0:
    broke_button = []
else: 
    broke_button = set(map(int, input().split())) # 고장난 버튼 집합
button = [str(x) for x in range(10) if x not in broke_button] # 정상 버튼 리스트(str형으로 저장)

answer = abs(100 - n) 

def dfs(depth, num):
    global answer
    answer = min(answer, abs(n - int(num)) + len(num)) # 숫자의 차이 + 숫자의 길이

    if depth == len(str(n))+1: # n 보다 자릿수가 1 높은 숫자 까지만 확인하기
        return
    
    for b in button: # 가능한 모든 버튼 눌러보기
        dfs(depth + 1, num + b)

for i in button:
    dfs(1, str(i)) 
print(answer)


# 두번째 풀이
n = int(input()) # 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수
if m == 0:
    broke_button = []
else:
    broke_button = set(input().split())

answer = abs(100 - n)

for num in range(1000001): # 0부터 모든 숫자 확인
    check = True # 가능한 숫자인지 여부

    # 한 숫자라도 고장난 버튼의 숫자라면 멈춤
    for b in str(num):
        if b in broke_button:
            check = False
            break
    if check:
        answer = min(answer, abs(n - num) + len(str(num)))

print(answer)