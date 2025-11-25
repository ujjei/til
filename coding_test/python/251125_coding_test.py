# 문제1. 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a+b}")


# 문제2. 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1+str2)

# 문제3.문자열 돌리기
str = input()
for i in str :
    print(i)

# 문제4. 홀짝 구분하기
a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 문제5. 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer