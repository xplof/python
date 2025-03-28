# 파이썬 타입
# bool type, int type, float type, str type



# if문은 반드시 "참"일 경우만 출력됨.
if True:
    print("참")
if 10>3:
    print("정상")
    

# 거짓일경우 출력x
if False:
    print("거짓")
if 10<3:
    print("거짓")
    

# print(1+2)
# print("안녕",1)
# print("숫자 : {:.2f}".format(10/3))

# print("1"+1) #에러. 앞은str 뒤는int
print(int("1")+1) #str타입을 int타입으로 변경해주면 가능
# 숫자형태 문자열만 숫자타입으로 변경가능


# 실수를 정수로 타입변경. 소수점 사라짐
# 숫자 타입변경 : int, float으로 변경가능
print(int(1.543435543543)) 
# 문자열 float타입을 int타입으로 변경은 안됨
print(float("11.1"))

print(str(1.665)) #모든 것을 문자열로 변경 가능


# 변수
# a=10 # =는 할당을 의미
# b=1.
# print(a+b)


# list타입 - 값을 여러개 저장
# lst=[1,2,3,4,5,5,6,6,7,7,8,8,8]
# print(lst)
# print(lst[0]+lst[1]+lst[2]+lst[3]+lst[3]+lst[4]+lst[5]+lst[6])
# lst.append(123)
# print(lst)

# input() : 데이터를 입력받는 명령어 - str1개
# score = input("데이터를 입력하세요 : ")
# print("입력 데이터 : ",score)

# 두 수 를 입력받아 합계 평균 출력
# num1= int(input("숫자를 입력하세요 : "))
# num2= int(input("숫자를 입력하세요 : "))
# print(num1+num2)

# score= int(input("점수를 입력하세요 : "))
# if score>=60:
#     print("합격")
# elif score>=50:
#     print("재시험")
# else:
#     print("불합격")
    
    
    
score= int(input("점수를 입력하세요 : "))
if score>=90: print("a")
elif score>=80:print("b")
elif score>=70:print("c")
elif score>=60:print("d")
elif score>=50:print("e")
else: print("f")