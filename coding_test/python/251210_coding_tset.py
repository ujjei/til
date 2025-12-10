# 문제 1. n의 배수
# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# a % b: 배수로 나누기

# 풀이

def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    else : answer = 0
    return answer


# 문제 2. 공배수
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 다른 사람의 풀이
# def solution(number, n, m):
#     return int(bool(number % n == 0) & bool(number % m == 0))

# 풀이
def solution(number, n, m):
    answer = 0
    if number%n + number%m == 0 :
        answer = 1
    else : answer = 0
    
    return answer


