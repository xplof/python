from stumodule import Student,Students
from stufunc import* #함수 변수 모두 다 가져옴

    
#학생성적프로그램
while True:
    choice=tmenu_print() #상단메뉴부분
    
    if choice==1:
        stu_input()#학생성적입력함수
               
    elif choice==2:
        stu_output() #학생성적출력함수

    elif choice==2:
