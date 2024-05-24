# #1. for문 - 문자열
# for i in "숭실대학교" :
#     print(i)

# #1-1. for문 - 리스트
# for i in ["봄", "여름", "가을", "겨울"] :
#     print(i, end = " ")

# #1-2.for문 - range
# for i in range(1, 11, 1) : #1부터 10까지
#     print(i)

# for i in range(11): #0부터 10까지
#     print(i)

# #1-2.for문을 while문으로
# n = 1 #변수선언필요
# while n <= 10:
#     print(n)
#     n += 1 #없으면무한반목문

# #1-3. 100까지의 합계를 구하시오.
# res = 0
# for i in range(1, 101, 1) :
#     res += i
# print(f"res = {res}, i = {i}")

# res = 0
# n = 1
# while n <= 100:
#     res += n
#     n += 1
# print(f"res = {res}, n = {n}")

# #1-4. 입력받은 수 까지의 합계를 구하시오
# res = 0
# input_num = int(input("정수입력: "))
# for i in range(1, input_num + 1, 1): #input_num + 1로 stop값 정하기
#     res += i
# print(res)

# n = 1
# res = 0
# while n <= input_num:
#     res += n
#     n += 1
# print(res)

# #1-5. 입력받은 수 중 홀수만 합하세요
# res = 0
# n = 1
# input_num = int(input("정수입력: "))
# while n <= input_num:
#     res += n
#     print(f"더해지는 값 = {n}")
#     n += 2
# print(res)
    
# res = 0
# for i in range(1, input_num + 1, 2):
#     res += i
#     print(f"더해지는 값 = {i}")
# print(res)

# res = 0
# for i in range(1, input_num + 1, 1):
#     if (i % 2 != 0):
#         res += i
#         print(f"더해지는 값 = {i}")
# print(res)

# #2. 구구단 출력
# for i in range(1, 10, 1): #9번 실행
#     for n in range(1, 10, 1): #9번 실행
#         print(f"{i} * {n} = {i * n}") #총 9*9 = 81회 실행

# #2-1. while 문으로 바꿔보세요
# i = 1
# while i <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{i} * {n} = {i * n}")
#         n += 1
#     i += 1

# #3. break문
# n = 1
# while n <= 20:
#     if (n % 5 == 0):
#         break
#     print(n)
#     n += 1

# print("===================")

# n = 1
# while n <= 20:
#     print(n)
#     if (n % 5 == 0):
#         break
#     n += 1

# print("===================")

# n = 1
# while n <= 20:
#     if (n % 5 == 0):
#         break
#     n += 1
#     print(n)

# #4. break 문
# while 1 :
#     num = int(input("숫자를 입력: "))
#     if num <= 0:
#         break
#     elif num % 2 == 0:
#         print(f"{num}은 짝수")
#     else:
#         print(f"{num}은 홀수")
