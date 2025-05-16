shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    #가장 비싼 가격이랑 가장 높은 할인율 매칭. 그리고 그 다음으로 큰 값이랑 그 다음으로 큰 할인율을 매칭. 내림차순 정렬 필요
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    # 1500000, 30000, 2000
    # 40, 20
    # 개수가 달라서 for문 말고 while문으로 접근
    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index +=1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))