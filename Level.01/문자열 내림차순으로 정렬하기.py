# 문자열 내림차순으로 배치하기
# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.
# 입출력 예
# s	         return
# "Zbcdefg"	"gfedcbZ"


## 나의 풀이~~
# def solution(s):
#     a = [i for i in s]
#     a.sort(reverse=True)
#     result = ''.join(a)
#     return result

# print(solution("Zbcdefg"))


## 나의 다른 풀이 (sort vs sorted)

def solution(s):
    a = sorted(s, reverse=True)
    b = ''.join(a)
    return b

print(solution("Zbcdefg"))

## 다른 사람 풀이
# def solution(s):
#     return ''.join(sorted(s, reverse=True))

