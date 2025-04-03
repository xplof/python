# import stu_func as stu #별칭사용
from stu_func import* #각각의 함수명 가져옴

students=[ #리스트타입
    {"no":1,"name": "홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100,"rank":1},
    {"no":2,"name": "유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
    {"no":3,"name": "이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1}
]
count=4
choice=0
title=['번호','이름','국어','영어','수학','합계','평균','등수']

        
        # 학생점수수정 함수선언
# def stu_modify()
# 함수사용의 목적
# 1. 중복된 코드의 재사용
# 2. 소스의 가독성 증대
# 화면출력 함수 선언


while True:
        #화면출력부분
    choice=stu_print()
    
    # 한줄복사 쉬프트 알트 방향키
    # 한줄삭제 컨 쉬 k
    # 쉬프트 방향키 - 칸선택
    
    if choice==1: # 학생성적입력부분
        count=stu_input(count,students)
        
    elif choice==2: #학생성적 출력부분
        stu_output(title,students)
        
    elif choice==3: #학생성적 수정부분
        print("[학생성적 수정]")
        name=input("수정하려고 하는 학생이름을 입력하세요 : ")
        temp=0 #못찾았을 때
        for s in students:
            if s['name']==name:
                temp=1
                print(f"{name}학생을 찾았습니다. 과목을 수정합니다.")
                print("[수정과목 선택]")
                print("1.국어")
                print("2.영어")
                print("3.수학")
                print("-"*10)
                choice=int(input("원하는 번호를 입력하세요 : "))
                sub_list=['','kor','eng','math']
                
                if choice==1:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                    s['total']=s['kor']+s["eng"]+s["math"]
                    s['avg']=s["total"]/3
                    print(f"변경 전 {title[choice+1]}점수 : {pre_score}, 변경 후 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    print()
                
                elif choice==2:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                    s['total']=s['kor']+s["eng"]+s["math"]
                    s['avg']=s["total"]/3
                    print(f"변경 전 {title[choice+1]}점수 : {pre_score}, 변경 후 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    print()
                
                elif choice==3:
                    pre_score=s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    s[sub_list[choice]]=int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                    s['total']=s['kor']+s["eng"]+s["math"]
                    s['avg']=s["total"]/3
                    print(f"변경 전 {title[choice+1]}점수 : {pre_score}, 변경 후 {title[choice+1]}점수 : {s[sub_list[choice]]}")
                    print()
                
                        
        if temp==0:
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요!!")
            print()
            
    elif choice==4:
        stu_rank(students) #등수처리
         # 등수처리 함수 선언

     
    elif choice==0:
        print("프로그램 종료")
        break
        
    
    