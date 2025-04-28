input = "abadabac"

def find_not_repeating_first_character(string):
    # 한번 쫙 훑어본다. 배열 인덱스로 몇번 나왔는지 넣어본다.
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    print(alphabet_occurrence_array)
    once_occurence_alphabet = []
    for index, count in enumerate(alphabet_occurrence_array):
        if count == 1:
            once_occurence_alphabet.append(chr(index + ord('a')))


    print(once_occurence_alphabet)

    for char in string:
        if char in once_occurence_alphabet:
            return char


    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))