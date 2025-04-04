# 화면출력 함수 선언
def stu_print():
    global choice
    print("[학생성적 프로그램]")
    print("-"*44)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("5. 학생성적정렬")
    print("6. 학생성적삭제")
    print("7. 학생성적저장")
    print("0. 프로그램종료")
    print("-"*44)
    choice=int(input("원하는 번호를 입력하세요 : "))
    return choice

# 1. 학생성적입력 함수선언
def stu_input(count,students):  
    no=count
    name=input(f"{no}번 학생이름을 입력하세요 : ")
    kor=int(input("국어점수를 입력하세요 : "))
    eng=int(input("영어점수를 입력하세요 : "))
    math=int(input("수학점수를 입력하세요 : "))
    total=kor+eng+math
    avg=total/3
    rank=0
    students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
    print(f"{no}번 {name}학생이 등록되었습니다.")
    count+=1   
    return count

# 학생성적출력 함수선언
def stu_output(title,students):
    print("[학생성적 출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
   


 # 등수처리 함수 선언
def stu_rank(students):
    print("[등수처리]")
    for s in students:
        num=1
        for ss in students:
            if s['total']<ss['total']: #등수 비교
                num+=1  #등수 1 증가
        s['rank']=num    #등수입력
    print("등수처리가 완료되었습니다.")
    print()