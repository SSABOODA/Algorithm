## 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3
# 입출력 예 설명
# 입출력 예 #1
# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

# 입출력 예 #2
# 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

# def solution(n):
#     s_num = []
#     x_num = []
#     for i in range(2 , n):
#         if n % i == 0:
#             x_num.append(n)
#         else:
#             s_num.append(n)
    
#     print(s_num)
#     print(x_num)
            
# print(solution(10))

import math

def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return len([ i for i in range(2, n+1) if array[i] ])

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

print(is_prime_number(26))