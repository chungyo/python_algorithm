top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # 5개 배열 생성
    # 더 큰 값에서만 수신함. 스택으로 풀기 가능?
    for height in range(len(heights)-1, -1, -1):  # 5개의 값이 나오겠지. 근데 뒤에서부터하자. 스택이니까
        height = heights.pop()
        for i in range(len(heights) -2, -1 ,-1):
            if height <= heights[i]:
                answer[len(heights)] = i + 2
                break

    return answer



print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))