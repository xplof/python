# # #이름,국어,영어,수학성적 입력받아 합계 및 평균 출력
# # # 이름 홍길동 합계300 평균 100.0
# # input("이름을 입력하세요 :")
# # a=input("국어 :")
# # b=input("수학 :")
# # c=input("영어 :")
# # a=float(a)
# # b=float(b)
# # c=float(c)
# # print("합계 :", a+b+c)
# # print("평균 :", (a+b+c)/3)

# # name = input("이름을 입력하세요 : ")
# # kor  = int(input("국어 점수를 입력하세요 : "))
# # eng  = int(input("영어 점수를 입력하세요 : "))
# # math  = int(input("수학 점수를 입력하세요 : "))
# # sci = int(input("과학 점수를 입력하세요 : "))
# # total= kor+eng+math+sci
# # avg= (kor+eng+math+sci)/4
# # print("이름 : ",name)
# # print("국어 : ",kor)
# # print("영어 : ",eng)
# # print("수학 : ",math)
# # print("과학 : ",sci)
# # print("합계 : ",total)
# # print("평균 : %.1f"% avg)


# # 프린트 시 - \n = 엔터, \t = 탭
# print("안녕하세요. \n반갑습니다. \t저는 홍길동입니다.")
# format() 문자형태지정

a=12
b=5
str_print="{}/{}={:.2f}".format(a,b,a/b)
str_print2 = f"{a}/{b}={(a/b):.2f}" #f함수 = foramt()
print(str_print2)


sss="{}".format(1)
print(sss)
print(type(sss))