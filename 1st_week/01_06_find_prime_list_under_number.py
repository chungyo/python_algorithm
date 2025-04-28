input = 20


def find_prime_list_under_number(number):
    prime_list = []
    # 소수는 자신과 1 외에는 나눌 수 없다.
    for n in range(2, number + 1):
       for i in prime_list:
           if n % i == 0:
               break
       else:
           prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)