# #1. retun이 필요: 합계 = 식이 존재 한다
# def price(n1, n2) :
#     커피 = 3000
#     차 = 4000
#     합계 = n1 * 커피 + n2 * 차
#     return 합계

# a = int(input("커피 개수: "))
# b = int(input("차 개수: "))

# res = price(a, b)
# print(res)

#############################

# #2. return이 필요없음
# def 홀짝구분(n):
#     if n % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# #2-1. return 문이 있도록
# def 홀짝구분(n):
#     if n % 2 == 0:
#         result = "짝수"
#     else:
#         result = "홀수"
#     return result

##############################

# #3. 매개변수가 없는
# def intro():
#     print("안녕하세요")
#     print("반갑습니다")

##############################

# #4-1. 입력받은 두 수의 곲을 구하는 함수
# def gop(a, b):
#     return a * b

# #4-2. 입력받은 두 수중 큰 수를 구하는 함수
# def kun(a, b):
#     if a >= b:
#         res = a
#     else:
#         res = b
#     return res

##############################

# #5-1. 모듈
# import webbrowser as w

# print("검색?")
# q = input("단어입력: ")
# url = f"www.google.com/search?q={q}"
# w.open(url)

# #5-2. 모듈
# import turtle as t

# def 각형(n):
#     for i in range(n):
#         t.forward(100)
#         t.right(360/n)

# a = int(input("원하는 각형 입력: "))

# t.shape("turtle")
# t.width(4)

# 각형(a)

###############################

# #6. 로또생성기
# import random
# for i in range(5):
#     num = []
#     while 1:
#         number = random.randint(1, 45)
#         if number not in num:
#             num.append(number)
#             if len(num) > 5:
#                 break
#     print(num)

# #6-2. 로또생성기 함수로 정의하자
# def 로또생성기():
#     import random
#     for i in range(5):
#         num = []
#         while 1:
#             number = random.randint(1, 45)
#             if number not in num:
#                 num.append(number)
#                 if len(num) > 5:
#                     break
#         print(num)
# 로또생성기()

# #etc
# import random

# numbers = []
# while len(numbers) < 6 : #6개 뽑자
#     number = random.randint(1, 45)
#     if number not in numbers:
#         numbers.append(number)

# print(numbers)

################################

