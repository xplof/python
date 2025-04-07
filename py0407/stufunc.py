from stumodule import Student,Students

# Students 객체선언
students=Students()
tilte=['번호','이름','국어','영어','수학','합계','평균','등수']

#상단메뉴부분
def tmenu_print():
    print("-"*20)
    print("[학생성적처리 프로그램]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("2. 프로그램종료")
    choice=0
    try:
        choice=int(input("번호입력 : "))
    except Exception as e:
        print(e)
    return choice

#학생성적입력함수선언
def stu_input():
    print("학생성적입력")
    name=input(f"{Student.count}번째 학생이름을 입력하세요 : ")
    score=[0]*3
    for i in range(len(score)):
        score[i]=int(input(f"{tilte[i+2]}점수를 입력하세요 : "))
    # kor=int(input("국어점수를 입력하세요 : "))
    # eng=int(input("영어점수를 입력하세요 : "))
    # math=int(input("수학점수를 입력하세요 : "))
    students.add(Student(name,*score))#score[0],score[1],score[3]))
    print(f"{name}학생이 등록되었습니다")
    print()
   
#학생성적출력함수선언
def stu_output():
    print("학생성적출력")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*tilte))
    print("-"*60)
    for s in students.students: #참조변수명.리스트변수
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}\t")
    
