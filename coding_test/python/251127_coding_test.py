###  answer= '' (str) / answer=0(int) / answer=[](list) 코테 템플릿
### 지금까지 배운 파이썬에서는 변수 선언 필요 x, 코테에서는 언어간의 중립성+오류 방지를 위해 변수 선언함

# 문제 1. 문자열 섞기

# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
def solution(str1, str2):
    ## 빈 문자열, 없으면 error
    answer = ''
    ## len(str1)=5
    ## range(0,5) / 0~4까지 5번 반복하게됨
    for i in range(0,len(str1)):
        ## 1번째 반복 ab
        ## 2번째 반복 abab
        answer = answer + str1[i] + str2[i]
    return answer



# 문제 2. 문자 리스트를 문자열로 변환하기

# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요

def solution(arr):
    answer = ''
    ## 구분자.join(리스트명) 구분자를 문자열 다 합쳐버리기
    answer = "".join(arr)
    return answer



# 문제 3. 문자열 곱하기

# 문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, k):
    return my_string*k



# 문제4. 더 크게 합치기

# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def solution(a, b):
    answer = 0
    # a+b, b+a정의
    answer1 = int(str(a)+str(b))
    answer2 = int(str(b)+str(a))
    # if문을 활용해서 a+b가 더 큰 경우 answer1로 출력 이외에는 모두 answer2로 출력
    if answer1 > answer2:
        answer = answer1
    else : 
        answer = answer2
    
    return answer



#문제 5. 두 수의 연산값 비교하기

# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

def solution(a, b):
    answer = 0
    answer1 = int(str(a)+str(b))
    answer2 = 2 * a * b
    
    if answer1 > answer2 : 
        answer = answer1
    elif answer2 > answer1 :
        answer = answer2
    else : answer = answer1
    
    return answer
