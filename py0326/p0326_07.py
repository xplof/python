# a=100
# b=50
# # 서로 값을 교체하려면?
# a=b
# b=a
# print(a) #50
# print(b) #50
# # A : 추가변수 c를 두고 값을 보관 후 교체
# c=a
# a=b
# b=c
# a,b=b,a #파이썬) ab 변수값 교체방법

# # 입력 - input
# print(input("숫자를 입력하세요"))
# # 변수에()있으면 함수 - 특정 기능구현을 말함
# # print()

a=input("1. 숫자를 입력하세요")
b=input("2. 숫자를 입력하세요")
print(a,b)
print(type(a))
print(type(b))
# 입력은 무조건 문자열str 타입
print(a+b)
# 타입변경 : 정수-int 실수-float 문자열-str 
# a=int(a) 
# b=int(b)
# print(a+b)
a=float(a)
b=float(b)
print(a+b)