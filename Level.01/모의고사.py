# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
# 입출력 예 설명
# 입출력 예 #1

# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# 입출력 예 #2

# 모든 사람이 2문제씩을 맞췄습니다.






def solution(answers):
    f_stu = [1,2,3,4,5]
    s_stu = [2,1,2,3,2,4,2,5]
    t_stu = [3,3,1,1,2,2,4,4,5,5]

    f_remainder = len(answers) % len(f_stu)
    s_remainder = len(answers) % len(s_stu)
    t_remainder = len(answers) % len(t_stu)
    
    f_share = len(answers) // len(f_stu)
    s_share = len(answers) // len(s_stu)
    t_share = len(answers) // len(t_stu)

    new_f_stu = (f_stu * f_share) + f_stu[0:f_remainder]
    new_s_stu = (s_stu * s_share) + s_stu[0:s_remainder]
    new_t_stu = (t_stu * t_share) + t_stu[0:t_remainder]
    score = [0,0,0]
    # f_score = 0
    # s_score = 0
    # t_score = 0
    # answer 개수 13 --> range(13) => 0~12
    for i in range(len(answers)):
        if answers[i] == new_f_stu[i]:
            score[0] += 1
        if answers[i] == new_s_stu[i]:
            score[1] += 1
        if answers[i] == new_t_stu[i]:
            score[2] += 1 
    

    answer = []
    max_score = max(score)
    for i in range(len(score)):
        if max_score == score[i]:
            answer.append(i+1)
            
    return answer
        
print(solution([1,2,3,4,5,1,2,3,4,5,1,2,3]))


##################다른 사람 정답#######################
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result
