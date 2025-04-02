# global 변수 : 전역변수
def func1():
    a=20


a=10
print("a :",a)
func1()
print("a :",a)



# s={"no":1,"name": "홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1}
# def cal(ss):
#     ss['kor']=int(input("수정할 국어점수를 입력하세요 : "))
#     ss['total']=ss['kor']+ss['eng']+ss['math']
#     ss['avg']=ss['total']/3
    
    
# print("학생성적 수정")    
# kor=100
# eng=100
# math=100

# 국어점수변경 함수호출
cal(s) #변경된 국어점수 입력됨
print("수정된 국어점수 :",s['kor'])
# 매개변수로 일반변수 전달형태 - return으로 값을 돌려줘서 입력시켜야함
# 국어점수변경 함수선언
# def cal(kor):
#     kor=int(input("수정할 국어점수를 입력하세요 : "))
#     return kor
    
# print("학생성적 수정")    
# kor=100
# eng=100
# math=100

# # 국어점수변경 함수호출
# kor=cal(kor) #변경된 국어점수 입력됨
# print("수정된 국어점수 :",kor)

# def cal(b_list):
#     b_list[0]=100
#     b_list[1]=200

# a_list=[0,0] #리스트타입변수 : 주소값
# a_list[0]=10
# a_list[1]=20
# print("함수호출 전 a_list :",a_list[0],a_list[1])

# cal(a_list)  #함수호출 b_list=a_list
# print("함수호출 후 a_list :",a_list[0],a_list[1])



# 함수 선언
# def cal(a,b):
#     a=100 #지역변수
#     b=200 #함수 내 변수선언은 새로운 저장공간을 만듬
#           #함수 내 일반변수는 함수를 벗어나면 사라짐
#           #bool,int,str,float
          
    
# #함수 밖
# a=10; b=20 #전역변수
# print("함수호출전 a,d :",a,b)

# # 함수호출
# cal(a,b)
# print("함수호출 후 :",a,b)

# # 이름,국어,영어,수학 점수를 입력받아 합계,평균을 출력하시오.
# students=[ #리스트타입
#     {"no":1,"name": "홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
#     {"no":2,"name": "유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
#     {"no":3,"name": "이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1}

# ]
# def stu_int():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
    
# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice=int(input("원하는 번호를 입력하세요 : "))
# if choice==2:
#     stu_int() #함수호출


# def cal(kor,eng,math):
#     # total=kor+eng+math
#     # avg=total/3
#     return kor+eng+math, (kor+eng+math)/3

# total,avg=cal(kor,eng,math)

# no=1
# name=input("이름을 입력하세요 : ")
# kor=int(input("국어 점수를 입력하세요 : "))
# eng=int(input("영어 점수를 입력하세요 : "))
# math=int(input("수학 점수를 입력하세요 : "))



# 직사각형 넒이와 둘레를 구하는 프로그램 구현
# 가로 세로를 입력받아 넓이와 둘레 구하기
# 함수 사용
# def cal(x,y):
#     result1=x*y
#     result2=x*2+y*2
#     return result1,result2

# x=int(input("가로 길이를 입력하세요"))
# y=int(input("세로 길이를 입력하세요"))
# result1,result2=cal(x,y)
# print("넓이 :",result1, "둘레 :", result2)
# cal 함수를 선언하시오
    # if n1%2==0:
    #     sum=sum+n1
    # if n2%2==0:
    #     sum=sum+n2
    # if n3%2==0:
    #     sum=sum+n3
    # if n4%2==0:
    #     sum=sum+n4
    # if n5%2==0:
    #     sum=sum+n5                
    # return sum
# 입력을 5개 받아 짝수만 모두 더한 값을 출력하시오
def cal(n_list):
    sum=0
    for n in n_list:
        if n%2==0:
            sum+=n
    return sum
n_list=[0]*5
for i in range(5):
    n_list[i]=int(input("숫자를 입력하세요 : "))
result=cal(n_list)
print("짝수의 합 :",result)


# 함수를 사용해서 두 수를 입력받아 
# 10~20 입력받으면 10+11+...+20값을 출력

# def add(n1,n2):
#     sum=0
#     if n1>n2:
#         c=n1
#         n1=n2
#         n2=c
#     for i in range(n1,n2+1):
#             sum=sum+i
#     print("합계 : ",sum)
    
   
# n1=int(input("숫자를 입력하세요 : "))
# n2=int(input("숫자를 입력하세요 : "))
# add(n1,n2)            
# add() 결과값을 출력하시오


# 함수사용
# 1. 중복코드가 있을때
# 2. 소스가 너무 복잡할때
# 먼저 프로그램 모두 구현 및 중복 확인 후 함수를 사용
 
# num1,num2,num3 값을 입력받아 합게와 평균 구하기
# def add(n1,n2,n3):
#     return n1+n2+n3

# n1= int(input("점수를 입력하세요 : "))
# n2= int(input("점수를 입력하세요 : "))
# n3= int(input("점수를 입력하세요 : "))
# total=add(n1,n2,n3)
# avg=total/3

# print(n1,n2,n3,total,avg)