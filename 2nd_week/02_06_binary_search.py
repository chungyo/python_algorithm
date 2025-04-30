finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    low = 0
    high = len(array) - 1
    mid = (low + high)// 2

    print(low, mid, high)
    while low <= high:
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high)// 2
    return False




result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)