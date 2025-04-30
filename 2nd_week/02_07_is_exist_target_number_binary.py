finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    # 바이너리 서치.
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2
    sorted_array = sorted(array)

    while low <= high:
        if sorted_array[mid] == target:
            return True
        elif target > sorted_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)