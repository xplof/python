a=int(input("1. 숫자를 입력하세요 : "))
b=int(input("2. 숫자를 입력하세요 : "))
tr_print1=f"{a}+{b}={a+b}"
tr_print2=f"{a}-{b}={a-b}"
tr_print3=f"{a}*{b}={a*b}"
tr_print4=f"{a}/{b}={a/b}"
print(tr_print1)
print(tr_print2)
print(tr_print3)
print(tr_print4)

kor=int(input("국어 점수를 입력하세요 : "))
eng=int(input("영어 점수를 입력하세요 : "))
math=int(input("수학 점수를 입력하세요 : "))
total=kor+eng+math
avg=(kor+eng+math)/3
# total=f"{kor}+{eng}+{math}={kor+eng+math}"
# avg=f"({kor}+{eng}+{math})/3={(kor+eng+math)/3}"
# print("합계 : ",total)
# print("평균 : ",avg)

total_score= "합계 : {}".format(total)
total_avg= "평균 : {:.2f}".format(avg) 
print(total_score)
print(total_avg)
