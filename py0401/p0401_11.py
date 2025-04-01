# title=['번호','이름','국어','영어','수학','합계','평균','등수']
# score=[0]*3 #kor,eng,math. append보다 미리 만들어두는게 빠름
# for i in range(3):
#     score[i]=int(input(f"{title[i+2]}점수를 입력하세요"))
# print(score)    

students=[
    {"no":1,"name": "홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name": "유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
    {"no":3,"name": "이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1}

]
count=4
title=['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*10,end="")
    print("[학생성적 프로그램]")
    print("-"*44)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    print("-"*44)   
    
    choice=int(input("원하는 번호를 입력하세요 : "))
    while True:
        if choice==1:
            print("학생성적입력")
            no=count
            name=input(f"{no}번 학생이름을 입력하세요(0. 이전화면 이동) : ")
            if name=='0': break
            
            kor=int(input("국어 성적을 입력하세요 : "))
            eng=int(input("영어 성적을 입력하세요 : "))
            math=int(input("수학 성적을 입력하세요 : "))
            total=kor+eng+math
            avg=total/3
            rank=0
            
            students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math,
                            "total":total, "avg":avg, "rank":rank})
            print(f"{name}학생성적이 등록되었습니다.")
            count+=1
            print()
            
        if choice==2:
            print("학생성적출력")
            print("{}/t{}/t{}/t{}/t{}/t{}/t{}/t{}/t".format(*title))
            for s in students:
                print(f"{s['no']}")
                