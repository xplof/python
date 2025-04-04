# import stu_func as stu #별칭사용
from stufunc import* #각각의 함수명 가져옴
import random

students=[]
# stu.txt파일에서 데이터 읽어와 sudents=[]데이터 입력시킴
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:         #여러줄일때 반복문 적용
        line=f.readline() #1줄 읽어오기
        if not line: break #데이터 없을때 종료
        s=line.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })
        
        
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
         
    elif choice==5: #학생성적정렬
        students2=[*students] #복사
        print("[학생성적정렬]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면이동")
        print("-"*30)
        choice=int(input("원하는 번호를 입력하세요 : "))
        if choice==1:
            students2.sort(key=lambda x:x['name'])
        elif choice==2:
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice==3:
            students2.sort(key=lambda x:x['total'])
        elif choice==4:
            students2.sort(key=lambda x:x['total'],reverse=True)
        elif choice==5:
            students2.sort(key=lambda x:x['no'])      
        elif choice==6:
            students2.sort(key=lambda x:x['no'],reverse=True)
        elif choice==0:continue
         
        stu_output(title,students2)
    
    
    elif choice==6: #학생성적삭제
        print("[학생성적삭제]")
        name=input("삭제하고자 하는 학생이름을 입력하세요 : ")
        temp=0
        for i,s in enumerate(students):
            if name==s['name']:
                temp=1
                print(f"{s['no']}번 {name}학생을 찾았습니다.")
                answer=input("학생성적을 삭제할까요?(삭제 시 복구불가)")
                if answer=="y":
                    del students [i]
                    print(f"{name}학생을 삭제했습니다.")
                    print()
                    break
        if temp==0:
            print(f"{name}학생을 찾지 못했습니다. 다시 입력하세요!")
            print()
            
        

    elif choice==7: #학생 성적 저장
        print("[학생성적저장]")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                line=f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다.")
        print()
        
    elif choice==0:
        print("프로그램 종료")
        break
        
    
    