################4주차###############

###############################
# 연필 = 2000
# 펜 = 3000

# 연필개수 = int(input("연필개수"))
# 펜개수 = int(input("펜개수"))

# 총합 = 연필 * 연필개수 + 펜 * 펜개수

# if 총합 >= 20000:
#     총합 = 총합 * 0.9

# print(총합)
###############################
# 나이 = int(input("나이 입력"))
# if 나이 >= 20:
#     print("성인")
# else:
#     print("미성년자")
###########################
# 주민번호_8번째자리 = int(input("주민번호 8번재 자리 입력"))
# if 주민번호_8번째자리 % 2 == 0:
#     print("여자")
# else:
#     print("남자")
##########################
# 나이 = int(input("나이입력"))

# if 나이 >= 10 :
#     if 나이 >= 20:
#         print("어른")
#     else:
#         print("학생")
# else:
#     print("아이")
######################
# 필기점수 = int(input("필기 점수 입력"))
# 코딩결과 = input("합격/불합격 입력")

# if (필기점수 >= 90) and (코딩결과 == "합격"):
#     print("합격")
# else:
#     print("불합격")

###################5주차#####################

########################
# 점수 = int(input("시험 결과 입력"))

# if 점수 >= 90:
#     print("A")
# elif 점수 >= 80:
#     print("B")
# elif 점수 >= 70:
#     print("C")
# else:
#     print("D")
#########################

#####################6주차####################

########################
# 어디까지 = int(input("어디까지합?"))
# sum = 0
# for i in range(1, 어디까지 + 1):
#     sum += i
# print(sum)

# i=1
# sum = 0
# while i <= 어디까지:
#     sum += i
#     i+=1
# print(sum) 
########################
# n = int(input("어디까지"))
# step = 1
# total = 0

# while step <= n:
#     total += step
#     step +=1
#######################
# list = ["val1", "val2", "val3"]
# n = 0
# while n < len(list):
#     print(list[n]) 
#     n += 1
#####################
# list = ["a", "b", "c"]
# for i in list:
#     print(i)
######################
# str = input("문자열입력")
# n = 1
# for i in str:
#     print(f"{n}번째 알파벳: {i}")
#     n += 1
######################

#######################7주차#####################

#####################
# n = 1
# while 1:
#     print(n)
#     if n % 5 == 0:
#         break
#     n += 1
#####################
# while 1:
#     n = int(input("양수입력"))
#     if n <= 0:
#         print("stop")
#         break
#     if n % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
#########################

###################8주차################

#######################
# list = ['a', 'b', ['c', 'd'], 10, [20, 30], True]
# print(len(list))
# print(['c'] in list)
# print(['20', '30'] in list)
# print('a' in list)
# #####################
# list = []
# list.append("a")
# list.append("b")
# list.append("c")
# append = input()
# list.append(append)
# print(list)

# del list[1]
# print(list)

# list.remove("c")
# print(list)
########################

###################9주차#################

#########################
# list = [10,20,30,40]
# print(min(list))
# print(sum(list))
########################
# set = {10,20,30}
# print(len(set))
# print(set)
########################3
# dictionary = {10: 100, 20: 200, 30: 300}
# print(dictionary.items())
###################

###################10주차###############3

#####################
# def is_even_or_odd(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# is_even_or_odd(10)

# def is_even_0r_0dd(num):
#     if num % 2 == 0:
#         result = "even"
#     else:
#         result = "odd"
#     return result

# print(is_even_0r_0dd(10))
######################
# def intro():
#     print("hi")
# intro()
#####################
# def gop():
#     n1 = int(input())
#     n2 = int(input())

#     gop = n1 * n2
#     return gop

# print(gop())

# a = int(input())
# b = int(input())

# def gop(n1, n2):
#     gop = n1 * n2
#     return gop

# print(gop(a, b))
##################
# a = int(input())
# b = int(input())

# def kun(n1, n2):
#     if a >= b:
#         return a
#     else:
#         return b
    
# print(kun(a, b))

#######################
# def order():
#     print("주문")
#     drink = input()
#     print(f"{drink} 주문하셨습니다")

# drink = input()
# cake = input()

# def print_order(drink, cake):
#     print(f"음료: {drink}, 케이크: {cake}")

# order()
# print_order(drink, cake)
########################
# # def order_list(n1, n2):
#     print(f"{n1}과 {n2}주문")

# n1 = input()
# n2 = input()
# order_list(n1, n2)
###########################
# from turtle import *

# def n각형(n):
#     for i in range(n):
#         forward(200)
#         right(360 / n)

# n = int(input())

# shape("turtle")
# width(3)
# n각형(n)

# for i in range(4):
#     forward(200)
#     right(90)

# n = int(input())
# for i in range(n):
#     forward(200)
#     right(360 / n)
######################