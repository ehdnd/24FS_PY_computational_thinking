import random

cpu_num = random.randint(1, 50)
user_num = 0
index = 0

while cpu_num != user_num:
    user_num = int(input("1부터 50 숫자 입력: "))
    index += 1
    if cpu_num > user_num:
        print("더 큰 숫자")
    elif cpu_num < user_num:
        print("더 작은 숫자")
    else:
        break
print(f"정답! 정답은 {cpu_num}이었습니다. {index}번만에 맞혔습니다. ")