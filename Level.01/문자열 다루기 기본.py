# 문자열 다루기 기본
# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# 입출력 예
# s	        return
# "a234"	false
# "1234"	true

## 나의 풀이 실패
def solution(s):
    try:
        if (len(s) == 4 or len(s) == 6) and int(s):
            return True
    except ValueError:
        return False

print(solution("a234"))

## 다른 사람 풀이
## s.digit() 랑 len() 함수의 자리 바꾸면 효율성 통과 가능!
def solution(s):
    if (len(s) == 4 or 6) and s.isdigit():
        return True
    else:
        return False

print(solution("a234"))

## 최종 정답 풀이
## String.isdigit() 을 통해서 해당 문자열이 숫자로만 이루어졌는지 확인할 수 있다.
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


