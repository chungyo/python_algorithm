input = "abcba"

# 소주만병만주소
def is_palindrome(string):
    #문자열의 길이를 찾고, low high값 인덱스로 저장. low랑 high는 각각 1씩 + 하다가 인덱스 값 같아지면 멈추고
    n = len(string)



    for i in range(n):
        if string[i] != string[n-1-i]:
            return False
    return True



    return True


print(is_palindrome(input))