# 달러를 입력하면 원화로 환산 후 출력
# 1$=1467원
# ,d = 천단위 콤마

# money=int(input("달러를 입력하세요 : "))
# won=money*1467
# print("입력한 달러 : {:,d}, 한화 : {:,d}".format(money,won))

# 1779원을 동전으로 변경.
# 500원 3개, 100원 2개, 50원 1개, 10원 2개, 1원 9개

# money=int(input("동전으로 변경할 금액을 입력하시오 : "))
# ch500=money//500
# ch100=(money%500)//100
# ch50=(money%500)%100//50
# ch10=(money%500)%100%50//10
# ch1=(money%500)%100%50%10//1
# print("500원{}개, 100원{}개, 50원{}개, 10원{}개, 1원{}개".format(ch500,ch100,ch50,ch10,ch1))

# # 원의 넓이 : 3.14 * r^2
# # 반지름을 입력받아 원의 넓이를 구하는 프로그램 구현
# # 출력 : 원의 넓이 : 100, 원의 둘레

# n1=int(input("반지름을 입력하세요 : "))
# n2=3.14*(n1**2)
# n3=2*3.14*n1
# print("원의 넓이 : {}cm2".format(n2))
# print("원의 둘레 : {}cm".format(n3))

# 사각형 가로, 세로 길이 입려받아 넓이 및 둘레 구하기
# n1=int(input("가로 길이를 입력하세요 : "))
# n2=int(input("세로 길이를 입력하세요 : "))
# print("넓이 : {}cm2".format(n1*n2))
# print("둘레 : {}cm".format((n1*2)+(n2*2)))

n=input("이름을 입력하세요 : ")
n1=int(input("국어 성적을 입력하세요 : "))
n2=int(input("영어 성적을 입력하세요 : "))
n3=int(input("수학 성적을 입력하세요 : "))
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print('-'*55)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(n,n1,n2,n3,(n1+n2+n3),((n1+n2+n3)/3)))


