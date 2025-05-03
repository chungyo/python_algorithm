input = [4, 6, 2, 9, 1]
# i = 0 j =0 일때는

def bubble_sort(array):
    # for문 2번 돌리는데 먼저 두개씩 비교하고 맨뒤에 부터 정렬된다고 생각하면됨.
    n = len(array) #5
    for i in range(n - 1): # i=0 j=0 n=5
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))