students=[
    [1,"홍길동",100,100,100,300,100,1],
    [2,"유관순",100,100,99,299,99.67,2],
    [3,"이순신",100,100,99,299,99.67,2]
]
# students=list()
count=4 #학생 번호를 생성
title=['번호','이름','국어','영어','수학','합계','평균','등수']

# 무한반복
while True:

    # 화면출력
    print("-"*40)
    print(" "*5,end="")
    print("[학생 성적 프로그램]")
    print("-"*40)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 검색")
    print("7. 등수처리")
    print("0. 프로그램 종료")
    print("-"*40)
    choice=int(input("원하는 번호를 입력하세요 : "))
    
    if choice==1:
        no=count #안해도 되지만 가독성을 위해   
        name=input(f"{no}번 학생 이름을 입력하세요 : ") 
        kor=int(input("국어 성적을 입력하세요 : "))
        eng=int(input("영어 성적을 입력하세요 : "))
        math=int(input("수학 성적을 입력하세요 : "))
        total=kor+eng+math
        avg=total/3
        rank=0
        
        students.append([no,name,kor,eng,math,total,avg,rank])
        count+=1
        print(f"{no}번 {name}학생이 등록되었습니다.")    
        
        

    elif choice==2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title)) #  *=전개연산자 깊은복사와 같은 개념
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*s))
            
            
    elif choice==3:
        print("학생 성적 수정")
        name=input("수정하려는 학생명을 입력하세요 :  ")
        temp=0
        for i,s in enumerate(students): #for i in studnets해도됨. 혹시몰라서 인덱스넘버 받아놓은것
            if name in s:
                temp=1
                print(f"{name}학생을 찾았습니다.")
                print("수정하려는 과목을 선택하세요")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                choice=int(input("원하시는 번호를 입력하세요 : "))
                if choice==1:
                   print("국어 성적 수정")
                   print(f"현재 국어 점수 : {}") 

                

        
    elif choice==1:
        pass
    elif choice==0:
        print("프로그램 종료")
        break