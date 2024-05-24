# #1. return
# def price(num):
#     price_drink = 2500
#     total_price = num * price_drink
#     return total_price


# #2. return 없는
# def is_even_or_odd(num):
#     if num % 2 == 0:
#         print(num, "is even")
#     else :
#         print(num, "is odd")

# #3. 수학의 함수느낌
# def f(x):
#     return x**2 + x + 1

# #4. 
# def average(num1, num2, num3):
#     result = (num1 + num2 + num3) / 3
#     return result

# #5. 안자, 반환겂 없음
# def order():
#     print("주문 음료 입력: ")
#     drink = input()
#     print(drink, "주문하셨습니다")

# #6. 반환값 없음
# def print_order(drink, cake):
#     print(f"음료: {drink}, 케이크: {cake}")

# #7. 람다함수 lambda함수
# def f(x ,y):
#     return x + y
# print(f(100, 200))

# print((lambda x, y : x + y) (100, 200))

# #8. lambda 함수 반복 사용
# lamsquare = lambda x : x**2
# print(lamsquare(5))

def etc():
    return 1,2
x = etc()
print(x)

a, b = etc()
print(a)
print(b)