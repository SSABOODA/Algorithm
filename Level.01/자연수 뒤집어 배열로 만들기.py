# 자연수 뒤집어 배열로 만들기
# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	return
# 12345	[5,4,3,2,1]


## 나의 풀이
# def solution(n):
#     str_num = str(n)
#     reverse_n = str_num[::-1]
    
#     a = [int(i) for i in reverse_n]

#     return a

## 나의 풀이 축약
def solution(n):
    a = [int(i) for i in str(n)][::-1]

    return a
print(solution(12345))

## 다른 사람 풀이

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))
