# 문제 설명
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.
# 입출력 예
# n	return
# 121	144
# 3	-1
# 입출력 예 설명
# 입출력 예#1
# 121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

# 입출력 예#2
# 3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.

## 나의 풀이
## math 함수 기억안나서 sqrt 구글링 했음..
import math
def solution(n):
    a = math.sqrt(n)
    b = int(a)
    if (a -b) == 0:
        return int((a+1)**2)
    else:
        return -1

print(solution(121))


# print(type(1.7320508075688772))
# print(type(11))

## 다른 사람 풀이
## 제곱근을 구할 떄 함수 안쓰고 0.5를 제곱 한다는 개념으로 접근 와우!!
## 제곱근이 아닌 수를 검사할 때 나머지가 0이 아닐 때? 라는 조건문으로 검사한 것도 와우!!
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1