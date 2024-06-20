money = int(input())                        # 현금
stock = list(map(int, input().split()))     # 주가

junhyun_m, seongmin_m = money, money        # 현금
junhyun_s, seongmin_s = 0, 0                # 주가

increase_cnt = 0    # 전일 대비 상승 횟수
decrease_cnt = 0    # 전일 대비 하락 횟수

for i in range(14):
    # 준현 전량 매수
    junhyun_s += junhyun_m // stock[i]
    junhyun_m -= (junhyun_m // stock[i]) * stock[i]
    
    # 성민
    if i > 0:
        if stock[i] > stock[i - 1]:
            increase_cnt += 1
            decrease_cnt = 0
        elif stock[i] < stock[i - 1]:
            decrease_cnt += 1
            increase_cnt = 0
        else:
            increase_cnt = 0
            decrease_cnt = 0
    # 성민 전량 매도
    if increase_cnt >= 3:
        seongmin_m += seongmin_s * stock[i]
        seongmin_s = 0
    # 성민 전량 매수
    if decrease_cnt >= 3:
        seongmin_s += seongmin_m // stock[i]
        seongmin_m -= (seongmin_m // stock[i]) * stock[i]

junhyun_result = junhyun_m + (stock[13] * junhyun_s)    # 마지막 날 자산
seongmin_result = seongmin_m + (stock[13] * seongmin_s)

if junhyun_result < seongmin_result:
    print("TIMING")
elif junhyun_result > seongmin_result:
    print("BNP")
else:
    print("SAMESAME")