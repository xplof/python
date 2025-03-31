# 초기화 선언
count=1
students=list()

# 프로그램 시작
while True:
    # 화면 출력
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
    print("0. 프로그램 종료")
    print("-"*30)
    
    # 번호입력
    choice=int(input("원하는 번호를 입력하세요 : "))
    print()
    
    # 원하는 프로그램 실행
    if choice==1:
        print("[학생 성적 입력]")
        no=count
        name=input("이름을 입력하세요 : ")
        kor=int(input("국어점수를 입력하세요 : "))
        eng=int(input("영어점수를 입력하세요 : "))
        math=int(input("수학점수를 입력하세요 : "))
        total=kor+eng+math
        avg=total/3
        rank=0
        student=[no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        count=count+1
        
    elif choice==2:
        print("                    [학생성적 프로그램]")
        print("-"*65)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for stu in students:
            for i,s in enumerate(stu):
                if i !=6: 
                    print(s,end="\t")
                else: #평균일때
                    print(f"{s:.2f}",end="\t")
            print()    
    elif choice==0:
        print('[프로그램 종료]') 
        break   
    print()