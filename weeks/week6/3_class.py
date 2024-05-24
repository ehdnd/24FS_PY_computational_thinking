# # 1. while 문 적용하기

# n = 1
# total = 0
# end_number = int(input("자연수 입력: "))

# while n <= end_number :
#     total = total + n
#     print(f"현재 더해진 값: {n}")
#     n += 1
#     print(f"현재 총 합: {total}")
#     print("=" * 10)

# print(f"최종 값: {total}")

#################################

# # 1-1. 수업

# n = 1
# sum = 0 #더한값저장변수
# num = int(input("더하고 싶은 최종 숫자를 입력: "))
# while n <= num :
#     sum = sum + n
#     n = n + 1

# print(sum)

#################################

# # 2. while문 적용하기1

# num = 0
# while num <= 10:
#     num = num + 2
# print(num)

# # 2. while문 적용하기2

# num = 1
# while (num <= 10):
#     print(num * num)
#     num += 1

# # 2. while문 적용하기3

# count = 1
# while (count <= 5):
#     print("ha")
#     count += 1

#################################

# # 3. while문 적용하기

# omelet = ["egg", "meat", "onion", "carrot"]
# n = 0

# while n < len(omelet):
#     ingredient = omelet[n]
#     print(ingredient)
#     n += 1

#################################

# # 4. while문 적용하기 (퀴즈)

# num = 5
# step = 0
# total = 2
# while step <= num :
#     total += step
#     step += 1

# print(total)

#################################


# # 5. for문 적용하기 (기타) (range)

# sum = 0     #100까지 합계구하기
# for i in range(101) :
#     sum = sum + i
# print(sum)

# # 5-1. for문 적용하기 (while 문으로 작성)
# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n = n + 1
# print(sum)

#################################

# 6. for문 적용하기 (기타) (시퀸스_리스트)

# lists = ["a", "b", "v"]
# for list in lists :
#     print(list)

#################################

# 7. for문 적용하기 (기타) (문자열)

# for i in "숭실대학교":
#     print(i)

#################################

# # 8. for문 적용하기 (기타)

# string = input("문자열 입력: ")
# strings = list(string)

# for i in strings :
#     print(f"{strings.index(i) + 1}번째 알파벳: {i}")

# # 8-1. for문 적용하기

# n = 1
# str = input("문자를 입력: ")

# for i in str:
#     print(n, "번째 알파벳:", i)
#     n = n + 1

#################################