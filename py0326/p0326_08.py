# # 두 숫자를 입력받아 합과 곱 출력
# # print(3+7)
# # print(3*7)
# # 213
# a=input("1. 숫자를 입력하세요")
# b=input("2. 숫자를 입력하세요")
# a=int(a)
# b=int(b)
# c=a
# a=b
# b=c
# print(a+b)
# print(a*b)
# print("두 수 출력 :", a,b)

a=100
st="안녕"
print("변수값 :",a)
print("변수값 :",st)
print("변수값 :" +st)
# print("변수값 :"+a) # 에러 - 다른타입을 +연산자와 사용 불가

a=10
b=5
print(a,"+",b,"=", a+b)
c=100
d=7
print(c,"+",d,"=", c+d)
print(c,"*",d,"=", c*d)
print("%d *%d = %d" % (c,d,c*d))
print(c,"/",d,"=",c/d)
print("%d / %d = %8.3f" % (c,d,c/d))