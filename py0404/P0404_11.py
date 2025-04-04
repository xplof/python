students=[]
# 파일읽어오기
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data=f.readline() 
        if not data  : break #빈 공백이면 반복문 종료
        s=data.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":s[7]
        })
#최대값 +1증가        
print(max(students,key=lambda x: x['no'])['no']+1)
title=['번호','이름','국어','영어','수학','합계','평균','등수']
count=0
while True:
    print("[학생성적 프로그램]")
    print("-"*44)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("7. 학생성적저장")
    print("0. 프로그램종료")
    print("-"*44)
    choice=int(input("원하는 번호를 입력하세요 : "))
    
    if choice==1:
        print("[학생성적 입력]")
        no=count
        name=input("이름을 입력하세요 : ")
        kor=int(input("국어점수를 입력하세요 : "))
        kor=int(input("국어점수를 입력하세요 : "))
        kor=int(input("국어점수를 입력하세요 : "))
        
        # students 저장
        students.append({
            "no":no,
            
        })
        print(f"{no}번{}학생이저장됨")
        print()
        count+=1
        
    if choice==2:
        print("[학생성적 출력]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
        print()    
        
    if choice==7:
        print("학생성적저장")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                data=f"{s['no']},{s['name']},{s['kot']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
                f.write(data)
        print("파일저장완료")
        print()