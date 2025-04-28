input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # for문 쓰는건 맞고, 연속 된다는 건 바로 다음 인덱스가 같은 숫자일 때, 하나의 배열에 담아둔다.
    # 모두 0으로 만들기
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1

    # 모두 1로 만들기
    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)