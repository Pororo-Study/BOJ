seed = int(input())
stock = list(map(int, input().split()))

def jun(seed, stock):
    count = 0
    for s in stock:
        # print(f'주식개수 : {count}, 잔고:{seed}')
        if seed > 0:
            c = seed // s
            count += c
            seed -= s*c
        
    return seed + stock[len(stock)-1] * count

def sung(seed, stock):
    up = 0
    down = 0
    count = 0
    for i in range(1,len(stock)):
        if stock[i-1] > stock[i]: # 하락 -> 매수
            down += 1
            # print(f'down : {down}')
            up = 0
            if down >= 3:
                c = seed // stock[i]
                count += c
                seed -= stock[i]*c
                # print(f'buy -> 주식개수 : {count}, 잔고:{seed}, 주식가격 : {stock[i]}')
        elif stock[i-1] < stock[i]: # 상승 -> 매도
            up += 1
            # print(f'up : {up}')
            down = 0
            if up >= 3:
                temp = count * stock[i]
                seed += temp
                count = 0
                # print(f'sell -> 주식개수 : {count}, 잔고:{seed}, 주식가격 : {stock[i]}')
        else:
            up = 0
            down = 0
    
    if up >= 2 and stock[len(stock)-2] < stock[len(stock)-1]:
        temp = count * stock[len(stock)-1]
        seed += temp
        count = 0
    if down >= 2 and stock[len(stock)-2] > stock[len(stock)-1]:
        temp = seed // stock[len(stock)-1]
        count += temp
        seed -= temp

    return seed + count * stock[len(stock)-1]


j = jun(seed, stock)
# print(f'자산:{j}')
s = sung(seed, stock)
# print(f'자산:{s}')

if j>s:
    print("BNP")
elif j<s:
    print("TIMING")
else:
    print("SAMESAME")