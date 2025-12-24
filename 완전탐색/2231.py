# 2231 분해합
# https://www.acmicpc.net/problem/2231

n = int(input())
check = False # 생성자 존재 여부

for i in range(1, 1000000, 1):
    total = i
    # 각 자리수의 합을 더하기
    s = str(i)
    for j in range(len(s)):
        total += int(s[j])

    if total == n:
        check = True
        print(i)
        break

if not check:
    print(0)