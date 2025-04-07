# 예외처리

# 1. 구문에러
# 2. 런타임에러

# priㅑnt("데이터 출력") #구문에러 오타
# a_list=[1,2,3,4,5]
# for a in a_list:
#     print(a)
# for i in range(6):
#     print(a_list[i]) #구문에 에러는없지만 실행시 에러 - 런타임에러
# 프로그램이 종료

# 에러 처리방법 - if조건문사용 , 예외처리사용

# print("1.학생성적출력")
# choice=(input("번호입력"))
# # 숫자로 변환가능한지확인
# if choice.isdigit():
#     choice=int(choice)
# else:
#     print("숫자만입력가능")
    
# print("입력번호 :",choice)


# 예외처리
print("1.학생성적출력")
choice=(input("번호입력"))
# 숫자로 변환가능한지확인
try: #예외처리 - 강제로 프로그램 종료되는 문제해결, 에러에대한 문제점확인
    choice=int(choice)
except Exception as e:
    print("숫자만입력가능")
    print(e) #에러의 구문을 출력가능
print("입력번호 :",choice)