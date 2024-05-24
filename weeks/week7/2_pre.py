# import time

# n = 1

# while n <= 5 :
#     print("파이썬 재밌네", n)
#     time.sleep(1)
#     n += 1

# print("파이썬 쉽네")

###########################

# import time

# n = 100

# while n <= 150 :
#     print("숫자", n)
#     time.sleep(0.3)
#     n += 5

# print("끝")

###########################

# n = 1

# print("구구단 3단")

# while n <= 9 :
#     print(f"3 x {n} = {3*n}")
#     n += 1

#############################

a = 1
n = int(input("구구단 몇단? 정수입력: "))

print(f"구구단 {n}단")

while a <= 9 :
    print(f"{n} x {a} = {n*a}")
    a += 1