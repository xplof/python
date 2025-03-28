# # 조건식
# a=int(input("숫자를 입력하세요 : "))
# if a<100:
#     print("조건이 참일때만 실행된다. a는 100보다 작다.")
#     print("다음 구문 실행")    
# else:
#     print("입력한 값은 100보다 큰 수입니다.")

# 양수인지 음수인지 확인. 0은 양수

# nn=int(input("숫자를 입력하세요 : "))
# if nn>=0:
#     print("양수입니다")
# else:
#     print("음수입니다")

n=int(input("숫자를 입력하세요 : "))
if n%2==0:
    print("짝수입니다")
    
else:
    print("홀수입니다")
if n%3==0:
    print("3의 배수입니다")
else:
    print("3의 배수가 아닙니다")
