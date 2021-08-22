# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 입출력 예
# n	lost	reserve	    return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	        4
# 3	[3]	    [1]	        2
# 입출력 예 설명
# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

# 출처

# ※ 공지 - 2019년 2월 18일 지문이 리뉴얼되었습니다.
# ※ 공지 - 2019년 2월 27일, 28일 테스트케이스가 추가되었습니다.
# ※ 공지 - 2021년 7월 28일 테스트케이스가 추가되었습니다.

## 나의 풀이
## 정답은 맞음
## 효율성 테스트 실패 (시간 복잡도??) or 다른 테스트 실패
# def solution(n, lost, reserve):
#     count = n-len(lost)
#     for i in reserve:
#         if (i+1 or i-1) in lost:
#             count += 1
    
#     return count



## 나의 풀이 222
## 비슷한 맥락이라 실패
# def solution(n, lost, reserve):
#     count = 0
#     for a, b in zip(lost, reserve):
#         if a - b == 1 or -1:
#             count += 1
    
#     return n-len(lost)+count

## 다른 사람 풀이
## 이것도 실팬데??
# def solution(n, lost, reserve):
#     reserve_n = list(set(reserve)-set(lost)) # [1]
#     lost_n    = list(set(lost)-set(reserve)) # [2,4]

#     count = n-len(lost)
#     for res in lost_n:
#         if res+1 in reserve_n:
#             count += 1
#             reserve_n.remove(res+1)
#         elif res-1 in reserve_n:
#             count += 1
#             reserve_n.remove(res-1)

#     return reserve_n, lost_n

## 한번 더 도전 
## 다른 사람 풀이고 이건 통과하네
def solution(n, lost, reserve):
    set_reserve = list(set(reserve)-set(lost)) # [1,3,5]
    set_lost    = list(set(lost)-set(reserve)) # [2,4]

    
    for i in set_reserve:# 그 왼쪽이 체육복이 없는 경우
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost: #그 오른쪽이 없는 경우
            set_lost.remove(i+1) 
    answer = n-len(set_lost)
    return answer



print(solution(3, [3], [1])) # 2
print(solution(5, [2,4], [3])) # 4
print(solution(5, [2,4], [1,3,5])) # 5

## 다른 사랆 풀이222222222222
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)