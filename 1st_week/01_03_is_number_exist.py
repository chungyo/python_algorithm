def is_number_exist(number, array):
    is_num_exist = False
    for num in range(len(array)):
        if number == array[num]:
            is_num_exist = True

    return is_num_exist


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))