# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.
# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]
# 입출력 예 설명
# 입출력 예 #1
# 위의 설명과 같습니다.

# 입출력 예 #2
# 자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.

## 나의 풀이
# def solution(n, m):
#     if (m > n) and (m % n == 0):
#         return [n, m]
#     elif (m < n) and (m % n == 0):
#         return [m, n]
#     else:
#         return [1, n*m]

#     # return [n, m] if m % n == 0 else [1, n*m]

# print(solution(1, 10))

## 다른 사람 풀이 
## 효율성 검사 에서 실패했다.
## 유클리드 호제법?을 꼭 사용하여 풀이하여야 한다.
## 아래 로직이 유클리드 호제법이다.!!
def gcd(n,m): # 5, 12 # 2, 5 # 1, 2
    mod = m % n # 2 = 12 % 5 # 1 = 5 % 2 # 0 = 2 % 1
    if mod != 0:
        m, n = n, mod # 12, 5 = 5, 2 # 5, 2 = 2, 1
        return gcd(n, m) # 2, 5 # 1, 2
    else:
        return n # 1

def solution(n,m):  # 5, 12
    return [gcd(n,m),int(m*n/gcd(n,m))]
   # return [1, 60/1]

print(solution(5, 12))

# 1 / 5 12
#     5 12
# 최대 공약수 = 1
# 최소 공배수 = 60

# 3 / 3 12
# 1 / 1 4
#     1 4
# 최대 공약수 = 3
# 최소 공배수 = 12

# 1 /  2 5
#      2 5
# 최대 공약수 = 1
# 최소 공배수 = 10

# 2 / 8 32
# 2 / 4 16
# 2 / 2 8
#     1 4
# 최대 공약수 = 8
# 최소 공배수 = 32