# a=123 
# print("입력된 숫자 :  %d" %(a))
# print("입력된 숫자 : {}".format(a))
# print(f"입력된 숫자 : {a}")
# 입력 - input타입 : str타입
# 입력된 값은  str타입이기 떄문에 형변환 필요

# input(123+123)
# n1=int(input("숫자를 입력하세요 : "))
# n2=int(input("숫자를 입력하세요 : "))
# print("입력된 숫자 : {},{} / 합계 : {}".format(n1,n2,n1+n2))

name=input("이름을 입력하세요 : ")
kor=int(input("국어 성적을 입력하세요 : "))
eng=int(input("영어 성적을 입력하세요 : "))
math=int(input("수학 성적을 입력하세요 : "))
total=kor+eng+math
avg=total/3
print("이름 : {}".format(name))
print("국어 성적 : {}".format(kor))
print("영어 성적 : {}".format(eng))
print("수학 성적 : {}".format(math))
print("합계 : {}".format(total))
print("평균 : {}".format(avg))
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*55)
print("{}\t{}\t{}\t{}\t{}\t{}".format(name,kor,eng,math,total,avg)
)






