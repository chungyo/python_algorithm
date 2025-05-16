prices = [1, 2, 3, 2, 3]
from collections import deque

def get_price_not_fall_periods(prices):
    queue = deque(prices)
    answer = []

    # 큐가 비어있지 않다면
    while queue:
        queue_not_fall_count = 0
        first = queue.popleft()
        for next_price in queue:
            if first <= next_price:
                queue_not_fall_count += 1
            else:
                queue_not_fall_count += 1
                break
        answer.append(queue_not_fall_count)

    return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))