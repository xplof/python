# 두 수를 입력받아 사칙연산을 출력하라
def cal(x,y):
    print("더하기:",x+y)
    print("빼기:",x-y)
    print("곱하기:",x*y)
    print("나누기:",x/y)
    return x+y

num1=int(input("첫번쨰 숫자를 입력하세요 : "))
num2=int(input("두번쨰 숫자를 입력하세요 : "))
result1=cal(num1,num2) #함수호출

num3=int(input("1번쨰 숫자를 입력하세요 : "))
num4=int(input("2번쨰 숫자를 입력하세요 : "))
result2=cal(num3,num4) #함수호출

num5=int(input("1번쨰 숫자를 입력하세요 : "))
num6=int(input("2번쨰 숫자를 입력하세요 : "))
result3=cal(num5,num6) #함수호출

# 결과중에 합계를 모두 더하고싶음
print("총 합계 :", result1+result2+result3)



# 함수
# def add(x,y):
#     print("x:",x)
#     print("y:",y)
#     print("x+y:",x+y)
    
# a=10
# b=20
# c=30
# d=40
# add(a,b)    
# add(a,c)





# def add():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
    
# print("누군가 오고 있어요")
# print("인사")
# add() #함수호출






























# print() #변수 뒤에 0가 있으면 함수
# def cal(x,y):
#     result=x+y
#     print(result)
#     result2=x-y
#     print(result2)
#     result3=x*y
#     print(result3)
#     result4=x/y
#     print(result4)

# a,b=10,20
# cal(a,b)

# c,d=100,200
# cal(c,d)


# e,f=50,100
# cal(e,f)