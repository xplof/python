title=['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("1. 국어입력")
    print("1. 영어입력")
    print("1. 수학입력")
    choice=int(input("원하는 번호를 입력하세요 : "))
    
    if choice==1:
        print("성적입력")
    
    elif choice==2:
        print("영어성적입력")
    
    elif choice==3:
        print("수학성적입력")